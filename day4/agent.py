# agent.py
import json
import re
from llm import chat
from tool_registry import get_tools_description, execute_tool
from memory.short_term import ShortTermMemory

SYSTEM_PROMPT_TEMPLATE="""你是一个智能助手，可以使用工具来帮助用户，也能记住对话历史。

{tools_description}

每次回复时，必须用 JSON 格式，选择以下两种之一：

使用工具：
{{"action": "use_tool", "tool": "工具名", "params": {{"参数名": "参数值"}}

直接回答：
{{"action": "answer", "content": "你的回答"}}

只返回JSON。

"""

def safe_parse_json(text: str) -> dict:
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    match = re.search(r'\{.*\}', text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group())
        except json.JSONDecodeError:
            pass
    return {"action": "answer", "content": text}


def build_system_prompt() -> str:
    # 动态生成，包含所有工具的说明
    tools_desc = get_tools_description()
    return f"""你是一个智能助手，可以使用工具来帮助用户。

{tools_desc}
每次回复时，必须用 JSON 格式，选择以下两种之一：

1. 如果需要使用工具：
{{"action": "use_tool", "tool": "工具名", "params": {{"参数名": "参数值"}}}}

2. 如果可以直接回答：
{{"action": "answer", "content": "你的回答"}}

参数名必须和工具定义完全一致（英文）。
只返回 JSON，不要加任何解释。"""

class Agent:
    def __init__(self)-> None:
        self.memory = ShortTermMemory(max_messages=20)
        # 系统提示只加一次，永远保留
        self.memory.add("system",SYSTEM_PROMPT_TEMPLATE.format(
            tools_description=get_tools_description()
        ))

    def chat(self,user_input:str)->str:
        # 用户输入存入记忆
        self.memory.add("user",user_input)

        # 调用LLM接口，传入完整对话历史
        ai_response = chat(self.memory.to_api_format())
        print(f"[AI 决策]:   {ai_response}")
        
        self.memory.add("assistant",ai_response)
        
        decision = safe_parse_json(ai_response)

        if decision["action"] == "answer":
            return decision.get("content", ai_response)

        if decision["action"] == "use_tool":
            tool_name = decision.get("tool", "")
            params = decision.get("params", {})
            print(f"[执行工具]:   {tool_name}，参数：{params}")
            result = execute_tool(tool_name, params)
            print(f"[工具结果]:   {result}")
        
            self.memory.add("user",
                f"[工具{tool_name} 返回结果]: {tool_result}\n"
                f"请基于此结果，用自然语言回答用户的问题。"
            )

            final = chat(self.memory.to_api_format())
            final_parsed = safe_parse_json(final)
            final_text = final_parsed.get("content",final)
            self.memory.add("assistant",final_text)
            
            return final_text

        return f"(未知 action：{decision.get('action')})"

    def clear(self)->None:
        self.memory.clear_non_system()
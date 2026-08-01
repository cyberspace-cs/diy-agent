from llm import chat

SYSTEM_PROMPT="""
你是一个智能助手

当用户问你问题时，判断：是直接回答，还是需要查天气

你必须使用JSON格式回复，不能说任何其他话。

格式如下：

如果可以直接回答：
{"action":"answer","content":"你的回答内容"}

如果需要查天气：
{"action":"get_weather","city":"城市名"}

只返回JSON，不要加任何解释、前缀或代码块标记。
"""

def run_agent(user_input:str)->str:
    messages=[
        {"role":"system","content":SYSTEM_PROMPT},
        {"role":"user","content":user_input},
    ]
    response=chat(messages)
    print(f"[AI决策]:{response}")
    return response
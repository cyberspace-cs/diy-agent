import re
import json

def get_weather(city:str)->str:
    """模拟天气数据，Day2换真实API"""
    mock_data={
        "北京":"晴，15℃，东风3级",
        "上海":"多云，18℃，南风4级",
        "广州":"小雨，22℃，东风"
    }
    return mock_data.get(city,f"{city}:晴，20℃（模拟数据）")

def safe_parse_json(text:str)->dict:
    """从AI回复里提取JSON，即使AI说了多余的话"""
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    match=re.search(r'\{.*\}',text.reDOTALL)
    if match:
        try:
            return json.loads(match.group())
        except json.JSONDecodeError:
            pass

    return {action:"answer",content:text}


def execute_action(ai_response:str)->str:
    """解析AI返回的JSON，执行对应动作"""
    decision=safe_parse_json(ai_response)
    action=decision.get("action")
    if action=="answer":
        return decision.get("content","AI回答失败")
    elif action=="get_weather":
        city=decision.get("city","未知城市")
        weather=get_weather(city)
        return f"{city}的天气是{weather}"
    else:
        return f"未知动作:{action!r}"

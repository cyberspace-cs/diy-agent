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

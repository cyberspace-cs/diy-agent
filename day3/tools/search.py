# tools/search.py
import requests
#https://cloud.baidu.com/doc/qianfan-api/s/Hmbu8m06u
import json
import os
BAIDU_API_KEY = os.getenv("BAIDU_API_KEY")


def web_search(query: str, max_results: int = 5) -> str:
    """用 Baidu 搜索，返回前几条结果。"""
    # url = "https://qianfan.baidubce.com/v2/ai_search/chat/completions"
    url = "https://qianfan.baidubce.com/v2/ai_search/web_search"
    
    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": query
            }
        ],
        "edition": "standard",
        "search_source": "baidu_search_v2",
        "search_recency_filter": "week"
    }, ensure_ascii=False)
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {BAIDU_API_KEY}'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload.encode("utf-8"))
    
    response.encoding = "utf-8"


    try:
        response.raise_for_status()
        data = response.json()


        # 提取 references 列表
        refs = data.get("references", [])
        if not refs:
            return f"没有找到关于「{query}」的搜索结果"
        
        # 只取前 max_results 条
        results = []
        for idx, item in enumerate(refs[:max_results], start=1):
            title = item.get("title", "无标题")
            snippet = item.get("snippet", "")
            source = item.get("website", "未知来源")
            # 摘要可能为空，用 snippet 代替
            content = item.get("content", snippet)
            results.append(
                f"{idx}. {title}\n   来源：{source}\n   摘要：{content[:150]}...\n"
            )

        return "\n".join(results)

    except requests.Timeout:
        return"搜索超时，请稍后重试或换个关键词"
    except Exception as e:
        return f"搜索出错：{e}"
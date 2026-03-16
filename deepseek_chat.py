# -*- coding: utf-8 -*-
"""
DeepSeek Chatbot: 火山引擎方舟接入 (Python 版)
"""

import json
import requests

# ===================== 【配置区域】 =====================
API_KEY = "4d084df8-7d7c-4c39-801e-98be61281a27"
BASE_URL = "https://ark.cn-beijing.volces.com/api/v3/responses"
MODEL_ID = "deepseek-v3-2-251201"
# ======================================================

def call_deepseek(user_query):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    # ✅ 严格符合火山方舟 v3/responses 接口的 input 格式
    data = {
        "model": MODEL_ID,
        "stream": False,
        "input": [
            {
                "role": "user",
                "content": user_query
            }
        ],
        "tools": []
    }

    try:
        response = requests.post(BASE_URL, headers=headers, json=data)
        print(f"【完整响应】: {response.text}")  # 先打印看结构
        if response.status_code == 200:
            result = response.json()
            # ✅ 先看返回结构再解析，这里用最通用的方式取 content
            if "output" in result and "choices" in result["output"]:
                return result["output"]["choices"][0]["message"]["content"]
            else:
                return f"返回结构不符: {result}"
        else:
            return f"[请求失败] 状态码 {response.status_code}：{response.text}"
    except Exception as e:
        return f"[调用异常] {str(e)}"

if __name__ == "__main__":
    print("🤖 DeepSeek Chatbot 已启动！输入 quit 退出\n")
    while True:
        query = input("你：")
        if query.lower() in ["quit", "exit"]:
            print("👋 对话结束。")
            break
        print("AI 正在思考...")
        reply = call_deepseek(query)
        print(f"AI：{reply}\n")
import requests
import os
import logging

API_URL = "https://open.bigmodel.cn/api/paas/v4/chat/completions"
logger = logging.getLogger(__name__)

def call_glm4_api(prompt):
    API_KEY = os.environ.get("API_KEY")  # 每次调用时都取
    try:
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        }
        data = {
            "model": "glm-4-flash",
            "messages": [{"role": "user", "content": prompt}],
            "stream": False
        }
        # 打印请求头和请求体
        print("=== GLM4 API 请求 ===")
        print("URL:", API_URL)
        print("Headers:", headers)
        print("Data:", data)
        response = requests.post(API_URL, headers=headers, json=data, timeout=30)
        print("Status Code:", response.status_code)
        print("Response Text:", response.text)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content']
    except Exception as e:
        logger.error(f"GLM4 API调用错误: {str(e)}")
        return f"Error: {str(e)}"

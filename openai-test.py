import requests
import os
import sys

# 从环境变量获取OpenAI API密钥
api_key = os.environ.get('API_KEY')
if not api_key:
    print("错误: 未设置API_KEY环境变量")
    print("请设置API_KEY环境变量再运行程序")
    sys.exit(1)

# The endpoint for the ChatGPT API
url = 'https://api.openai.com/v1/chat/completions'

# The headers for the request
headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json',
}

# The data for the request
data = {
    'model': 'gpt-4o',  # or 'gpt-4', depending on your access
    'messages': [
        {'role': 'user', 'content': 'tell me how to survive as a PhD in a good university'}
    ]
}

# Make the POST request to the API
response = requests.post(url, headers=headers, json=data)

# Print the response from the API
if response.status_code == 200:
    response_data = response.json()
    print("ChatGPT response:", response_data['choices'][0]['message']['content'])
else:
    print(f"Error: {response.status_code}")
    print(response.text)

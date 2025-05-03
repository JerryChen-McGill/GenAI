from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import requests
import os
import sys

app = Flask(__name__)
CORS(app)

# 从环境变量获取OpenAI API密钥
api_key = os.environ.get('API_KEY')
if not api_key:
    print("错误: 未设置API_KEY环境变量")
    print("请设置API_KEY环境变量再运行程序")
    sys.exit(1)

# Function to call OpenAI API
def call_chatgpt_api(prompt):
    url = 'https://api.openai.com/v1/chat/completions'
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json',
    }
    data = {
        'model': 'gpt-4',  # or 'gpt-3.5-turbo' depending on your plan
        'messages': [
            {'role': 'user', 'content': prompt}
        ]
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return "Error: " + response.text

# Route to serve the HTML file
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# Route to handle problem generation requests
@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    grade = data.get('grade')
    topic = data.get('topic')
    
    prompt = f"Give me 5 math problems for {grade} grade about {topic}."
    problems = call_chatgpt_api(prompt)
    
    return jsonify({'problems': problems})

# 运行 Flask 应用
if __name__ == '__main__':
    # 获取端口号（云平台通常会提供PORT环境变量）
    port = int(os.environ.get('PORT', 5000))
    # 启动 Flask 应用
    app.run(debug=False, host='0.0.0.0', port=port)
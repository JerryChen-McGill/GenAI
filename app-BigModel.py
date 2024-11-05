from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

# 智谱清言 API endpoint and key
API_KEY = "fe760163c5256f75c27653c2fd729bec.Zt93rQwt99u8n8zV"
API_URL = "https://open.bigmodel.cn/api/paas/v4/chat/completions"

def call_glm4_api(prompt):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    
    data = {
        "model": "glm-4-flash",
        "messages": [{"role": "user", "content": prompt}],
        "stream": False
    }
    
    response = requests.post(API_URL, headers=headers, json=data)
    
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return f"Error: {response.status_code} - {response.text}"

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    grade = data.get('grade')
    difficulty = data.get('difficulty')
    number = data.get('number')
    topic = data.get('topic')
    requirements = data.get('requirements')
    
    prompt = f"Generate {number} math problems for {grade}th grade students about {topic}. The difficulty level should be {difficulty}. Additional requirements: {requirements}"
    problems = call_glm4_api(prompt)
    
    return jsonify({'problems': problems})

if __name__ == '__main__':
    # 启动 Flask 应用，监听所有 IP 地址的 5000 端口
    app.run(debug=True, host='0.0.0.0', port=5000)

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

# 从环境变量获取API密钥
API_KEY = os.environ.get("API_KEY", "fe760163c5256f75c27653c2fd729bec.Zt93rQwt99u8n8zV")
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
    # 获取端口号（云平台通常会提供PORT环境变量）
    port = int(os.environ.get("PORT", 5000))
    # 启动 Flask 应用
    app.run(debug=False, host='0.0.0.0', port=port)

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

# Your OpenAI API key
api_key = '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'

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
    app.run(debug=True)
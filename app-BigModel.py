from flask import Flask, request, jsonify, send_from_directory, redirect
from flask_cors import CORS
import requests
import os
import sys
import logging
from dotenv import load_dotenv

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 加载.env文件中的环境变量
load_dotenv('APIkey.env')

app = Flask(__name__)
# 配置CORS，允许所有来源
CORS(app, resources={r"/*": {"origins": "*"}})

# 从环境变量获取API密钥
API_KEY = os.environ.get("API_KEY")
if not API_KEY:
    logger.error("错误: 未设置API_KEY环境变量")
    sys.exit(1)

API_URL = "https://open.bigmodel.cn/api/paas/v4/chat/completions"

def call_glm4_api(prompt):
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
        
        response = requests.post(API_URL, headers=headers, json=data, timeout=30)
        response.raise_for_status()
        
        return response.json()['choices'][0]['message']['content']
    except requests.exceptions.RequestException as e:
        logger.error(f"API调用错误: {str(e)}")
        return f"Error: API request failed - {str(e)}"
    except Exception as e:
        logger.error(f"未知错误: {str(e)}")
        return f"Error: An unexpected error occurred - {str(e)}"

@app.route('/')
def index():
    return send_from_directory('.', 'personalization.html')

@app.route('/main')
def main():
    return send_from_directory('.', 'index.html')

@app.route('/personalization')
def personalization():
    return send_from_directory('.', 'personalization.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('.', path)

@app.route('/check-preferences')
def check_preferences():
    return jsonify({'hasPreferences': True})

@app.route('/generate', methods=['POST'])
def generate():
    try:
        data = request.json
        logger.info(f"Received request data: {data}")
        
        if not data:
            logger.error("No data provided in request")
            return jsonify({'error': 'No data provided'}), 400

        # 验证输入数据
        required_fields = ['grade', 'difficulty', 'number', 'topic']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            error_msg = f'Missing required fields: {", ".join(missing_fields)}'
            logger.error(error_msg)
            return jsonify({'error': error_msg}), 400

        # 验证数值范围
        try:
            number = int(data['number'])
            if number < 1 or number > 10:
                error_msg = 'Number of problems must be between 1 and 10'
                logger.error(error_msg)
                return jsonify({'error': error_msg}), 400
        except (ValueError, TypeError):
            error_msg = 'Number of problems must be a valid integer'
            logger.error(error_msg)
            return jsonify({'error': error_msg}), 400

        grade = data.get('grade')
        difficulty = data.get('difficulty')
        topic = data.get('topic')
        requirements = data.get('requirements', '')
        selected_tags = data.get('selectedTags', [])
        
        # 构建包含标签的提示词
        tags_context = ""
        if selected_tags:
            tags_context = f" The problems should incorporate these interests: {', '.join(selected_tags)}."
        
        prompt = f"""Generate {number} math problems for {grade}th grade students about {topic}. 
The difficulty level should be {difficulty}.{tags_context}
Additional requirements: {requirements}

Please format the problems clearly with:
1. Problem statement
2. Step-by-step solution
3. Final answer

Make the problems engaging and relatable to the student's interests."""
        
        logger.info(f"Generated prompt: {prompt}")
        problems = call_glm4_api(prompt)
        return jsonify({'problems': problems})
    except Exception as e:
        logger.error(f"生成问题时发生错误: {str(e)}", exc_info=True)
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    # 生产环境中禁用debug模式
    debug_mode = os.environ.get("FLASK_ENV") == "development"
    app.run(debug=debug_mode, host='0.0.0.0', port=port)

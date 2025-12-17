from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import sys
import logging
from dotenv import load_dotenv
import re

# 1. 先加载dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), '../APIkey.env')
print("加载dotenv路径：", dotenv_path)
load_dotenv(dotenv_path)
print("API_KEY from env:", os.environ.get("API_KEY"))

# 2. 再import依赖API_KEY的模块
from api_glm4 import call_glm4_api
# from api_chatgpt import call_chatgpt_api  # 以后可加

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 指定前端静态文件目录
FRONTEND_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), '../frontend'))
print("FRONTEND_FOLDER:", FRONTEND_FOLDER)

app = Flask(__name__, static_folder=FRONTEND_FOLDER, template_folder=FRONTEND_FOLDER)
CORS(app, resources={r"/*": {"origins": "*"}})

# 检查API_KEY
if not os.environ.get("API_KEY"):
    logger.error("错误: 未设置API_KEY环境变量")
    sys.exit(1)

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'login.html')

@app.route('/login')
def login():
    return send_from_directory(app.static_folder, 'login.html')

@app.route('/main')
def main():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/personalization')
def personalization():
    return send_from_directory(app.static_folder, 'personalization.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

@app.route('/check-preferences')
def check_preferences():
    return jsonify({'hasPreferences': True})

@app.route('/generate', methods=['POST'])
def generate():
    try:
        data = request.json
        logger.info(f"Received request data: {data}")
        print("收到/generate请求，参数：", data)
        
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
### Problem Statement
[Your problem statement here]

### Hints
[Your hints here]

### Step-by-Step Solution
[Your step-by-step solution here]

### Final Answer
[Your final answer here]

Make the problems engaging and relatable to the student's interests."""
        
        logger.info(f"Generated prompt: {prompt}")

        # 选择API（这里可以根据前端传参或配置切换）
        api_type = data.get('api_type', 'glm4')
        if api_type == 'glm4':
            response = call_glm4_api(prompt)
        # elif api_type == 'chatgpt':
        #     response = call_chatgpt_api(prompt)
        else:
            return jsonify({'error': 'Unknown API type'}), 400

        # 分割响应内容
        parts = {
            'problem': '',
            'hints': '',
            'solution': '',
            'answer': ''
        }
        
        # 使用正则表达式分割内容
        problem_match = re.search(r'### Problem Statement\s*(.*?)(?=### Hints|$)', response, re.DOTALL)
        if problem_match:
            parts['problem'] = problem_match.group(1).strip()
        hints_match = re.search(r'### Hints\s*(.*?)(?=### Step-by-Step Solution|$)', response, re.DOTALL)
        if hints_match:
            parts['hints'] = hints_match.group(1).strip()
        solution_match = re.search(r'### Step-by-Step Solution\s*(.*?)(?=### Final Answer|$)', response, re.DOTALL)
        if solution_match:
            parts['solution'] = solution_match.group(1).strip()
        answer_match = re.search(r'### Final Answer\s*(.*?)$', response, re.DOTALL)
        if answer_match:
            parts['answer'] = answer_match.group(1).strip()
        
        return jsonify({
            'problem': parts['problem'],
            'hints': parts['hints'],
            'solution': parts['solution'],
            'answer': parts['answer']
        })
    except Exception as e:
        logger.error(f"生成问题时发生错误: {str(e)}", exc_info=True)
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    debug_mode = os.environ.get("FLASK_ENV") == "development"
    app.run(debug=debug_mode, host='0.0.0.0', port=port)

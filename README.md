# Math Problem Generator

An AI-powered math problem generator that creates personalized math problems based on user interests and preferences.

## Online Usage

Visit https://genai-oac9.onrender.com/ to use the application online.

## Features

- **Personalized Problem Generation**: Generate math problems tailored to your interests and hobbies
- **Detailed Solutions**: Step-by-step solutions and hints for each problem
- **Favorite Questions**: Save and manage your favorite problems
- **Prompt Settings**: Save and reuse your problem generation settings

## Tech Stack

- **Backend**: Python Flask
- **Frontend**: HTML, CSS, JavaScript (Vanilla JS, Vue.js 3)
- **Authentication**: Firebase Authentication
- **AI**: GLM4 API (Zhipu AI)
- **Storage**: localStorage, Firebase Firestore

## Local Setup

1. **Clone the repository:**
```bash
git clone [repository-url]
cd Math-Problem-Generator
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables:**
   Create `APIkey.env` file in the project root and add:
   ```
   API_KEY=your_api_key_here
   ```
   See `API_SETUP.md` for detailed instructions.

4. **Run the application:**
```bash
python backend/app.py
```

5. **Access the application:**
   Open your browser and navigate to `http://localhost:5000`

## Contributing

Contributions are welcome! Please feel free to submit Issues and Pull Requests.

## License

MIT License

---

# 数学题目生成器

基于人工智能的数学题目生成器，可根据用户兴趣和偏好生成个性化数学题目。

## 在线使用

访问 https://genai-oac9.onrender.com/ 即可在线使用。

## 功能特点

- **个性化题目生成**：根据您的兴趣和爱好生成定制化的数学题目
- **详细解答**：为每道题目提供分步解答和提示
- **收藏题目**：保存和管理您喜欢的题目
- **提示设置**：保存和重复使用您的题目生成设置

## 技术栈

- **后端**：Python Flask
- **前端**：HTML, CSS, JavaScript (原生 JS, Vue.js 3)
- **认证**：Firebase Authentication
- **AI**：GLM4 API (智谱AI)
- **存储**：localStorage, Firebase Firestore

## 本地运行

1. **克隆仓库：**
```bash
git clone [repository-url]
cd Math-Problem-Generator
```

2. **安装依赖：**
```bash
pip install -r requirements.txt
```

3. **设置环境变量：**
   在项目根目录创建 `APIkey.env` 文件并添加：
   ```
   API_KEY=your_api_key_here
   ```
   详细说明请参考 `API_SETUP.md`。

4. **运行应用：**
```bash
python backend/app.py
```

5. **访问应用：**
   打开浏览器，访问 `http://localhost:5000`

## 贡献

欢迎贡献！请随时提交 Issue 和 Pull Request。

## 许可证

MIT License

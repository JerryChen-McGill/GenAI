# Math Problem Generator

An AI-powered math problem generator that creates personalized math problems based on user interests and preferences.

## Features

- **Personalized Problem Generation**: Generate math problems tailored to your interests and hobbies
- **Multiple Math Topics**: Support for algebra, geometry, probability, and more
- **Difficulty Levels**: Adjustable difficulty from easy to challenging
- **Detailed Solutions**: Step-by-step solutions and hints for each problem
- **User Authentication**: Secure login and registration with Firebase
- **Favorite Questions**: Save and manage your favorite problems
- **Prompt Settings**: Save and reuse your problem generation settings
- **Interest Preferences**: Customize your learning experience based on your interests

## Local Setup

### Prerequisites

- Python 3.7+
- pip

### Installation Steps

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
   - Create `APIkey.env` file in the project root
   - Add your API key:
   ```
   API_KEY=your_api_key_here
   ```
   - See `API_SETUP.md` for detailed setup instructions

4. **Run the application:**
```bash
python backend/app.py
```

5. **Access the application:**
   - Open your browser and navigate to `http://localhost:5000`
   - The main page will be displayed directly

## Online Usage

Visit [Render deployment link] to use the application online.

## Tech Stack

- **Backend**: Python Flask
- **Frontend**: HTML, CSS, JavaScript (Vanilla JS, Vue.js 3)
- **Authentication**: Firebase Authentication
- **AI**: GLM4 API (Zhipu AI)
- **Storage**: localStorage, Firebase Firestore (for future features)

## Project Structure

```
Math Problem Generator/
├── backend/
│   ├── app.py              # Main Flask application
│   ├── api_glm4.py         # GLM4 API integration
│   └── ...
├── frontend/
│   ├── index.html          # Main problem generation page
│   ├── login.html          # Login and registration page
│   ├── personalization.html # User preference settings
│   ├── styles.css          # Global styles
│   └── firebase-config.js  # Firebase configuration
├── requirements.txt        # Python dependencies
├── API_SETUP.md           # API setup guide
└── README.md              # This file
```

## Features in Detail

### User Authentication
- Secure registration and login with Firebase
- User profile management
- Session management

### Problem Generation
- Input topic, grade level, and difficulty
- Add custom tags and requirements
- Generate personalized math problems with AI

### Question Management
- Save favorite questions to localStorage
- View saved questions in sidebar
- Import saved prompt settings

### Personalization
- Set your interests and hobbies
- Customize learning preferences
- View and manage your interest settings

## Contributing

Contributions are welcome! Please feel free to submit Issues and Pull Requests.

## License

MIT License

---

# 数学题目生成器

基于人工智能的数学题目生成器，可根据用户兴趣和偏好生成个性化数学题目。

## 功能特点

- **个性化题目生成**：根据您的兴趣和爱好生成定制化的数学题目
- **多种数学主题**：支持代数、几何、概率等多个数学领域
- **难度级别**：可调节难度，从简单到挑战性
- **详细解答**：为每道题目提供分步解答和提示
- **用户认证**：使用 Firebase 进行安全的登录和注册
- **收藏题目**：保存和管理您喜欢的题目
- **提示设置**：保存和重复使用您的题目生成设置
- **兴趣偏好**：根据您的兴趣定制学习体验

## 本地运行

### 前置要求

- Python 3.7+
- pip

### 安装步骤

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
   - 在项目根目录创建 `APIkey.env` 文件
   - 添加您的 API 密钥：
   ```
   API_KEY=your_api_key_here
   ```
   - 详细设置说明请参考 `API_SETUP.md`

4. **运行应用：**
```bash
python backend/app.py
```

5. **访问应用：**
   - 打开浏览器，访问 `http://localhost:5000`
   - 主页将直接显示

## 在线使用

访问 [Render 部署链接] 即可在线使用。

## 技术栈

- **后端**：Python Flask
- **前端**：HTML, CSS, JavaScript (原生 JS, Vue.js 3)
- **认证**：Firebase Authentication
- **AI**：GLM4 API (智谱AI)
- **存储**：localStorage, Firebase Firestore (用于未来功能)

## 项目结构

```
Math Problem Generator/
├── backend/
│   ├── app.py              # Flask 主应用
│   ├── api_glm4.py         # GLM4 API 集成
│   └── ...
├── frontend/
│   ├── index.html          # 题目生成主页面
│   ├── login.html          # 登录注册页面
│   ├── personalization.html # 用户偏好设置
│   ├── styles.css          # 全局样式
│   └── firebase-config.js  # Firebase 配置
├── requirements.txt        # Python 依赖
├── API_SETUP.md           # API 设置指南
└── README.md              # 本文件
```

## 功能详情

### 用户认证
- 使用 Firebase 进行安全的注册和登录
- 用户资料管理
- 会话管理

### 题目生成
- 输入主题、年级和难度
- 添加自定义标签和要求
- 使用 AI 生成个性化数学题目

### 题目管理
- 将喜欢的题目保存到 localStorage
- 在侧边栏查看已保存的题目
- 导入已保存的提示设置

### 个性化设置
- 设置您的兴趣和爱好
- 自定义学习偏好
- 查看和管理您的兴趣设置

## 贡献

欢迎贡献！请随时提交 Issue 和 Pull Request。

## 许可证

MIT License

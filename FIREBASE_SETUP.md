# Firebase Authentication 设置指南

## 📚 概述

这个指南将帮助你设置 Firebase Authentication，实现用户登录/注册功能。

## 🚀 第一步：创建 Firebase 项目

1. 访问 [Firebase Console](https://console.firebase.google.com/)
2. 点击"添加项目"或"创建项目"
3. 输入项目名称（如：math-problem-generator）
4. 选择是否启用 Google Analytics（可选）
5. 点击"创建项目"

## 🔐 第二步：启用 Authentication

1. 在 Firebase Console 中，点击左侧菜单的"Authentication"
2. 点击"Get started"（开始使用）
3. 点击"Sign-in method"（登录方式）标签
4. 点击"Email/Password"（邮箱/密码）
5. 启用"Email/Password"提供者
   - 启用第一个开关（Email/Password）
   - 可选：启用第二个开关（Email link - 邮箱链接登录）
6. 点击"Save"（保存）

## 📱 第三步：获取 Web 应用配置

1. 在 Firebase Console 中，点击项目设置（齿轮图标）
2. 滚动到"Your apps"（你的应用）部分
3. 点击 Web 图标（</>）
4. 输入应用昵称（如：Math Problem Generator Web）
5. 可选：设置 Firebase Hosting
6. 点击"Register app"（注册应用）
7. 复制配置对象，它看起来像这样：

```javascript
const firebaseConfig = {
  apiKey: "AIzaSy...",
  authDomain: "your-project.firebaseapp.com",
  projectId: "your-project-id",
  storageBucket: "your-project.appspot.com",
  messagingSenderId: "123456789",
  appId: "1:123456789:web:abcdef"
};
```

## ⚙️ 第四步：配置项目

1. 打开 `frontend/firebase-config.js`
2. 将你从 Firebase Console 复制的配置替换到 `firebaseConfig` 对象中：

```javascript
const firebaseConfig = {
    apiKey: "你的_API_KEY",
    authDomain: "你的项目ID.firebaseapp.com",
    projectId: "你的项目ID",
    storageBucket: "你的项目ID.appspot.com",
    messagingSenderId: "你的发送者ID",
    appId: "你的应用ID"
};
```

## 🧪 第五步：测试

1. 启动后端服务器：
```bash
cd backend
python app.py
```

2. 在浏览器访问：
   - 登录页面：`http://localhost:5000/login`
   - 或主页：`http://localhost:5000/`（会自动重定向到登录页）

3. 测试功能：
   - 注册新账户
   - 登录
   - 访问个性化设置页面（需要登录）

## 📖 Firebase Authentication 工作原理

### 1. 用户注册流程

```
用户输入邮箱和密码
    ↓
前端调用 createUserWithEmailAndPassword()
    ↓
Firebase 验证输入
    ↓
创建用户账户（存储在 Firebase 后端）
    ↓
自动登录用户
    ↓
返回 User 对象和 ID Token
    ↓
触发 onAuthStateChanged 监听器
```

### 2. 用户登录流程

```
用户输入邮箱和密码
    ↓
前端调用 signInWithEmailAndPassword()
    ↓
Firebase 验证凭证
    ↓
创建会话（Session）
    ↓
返回 User 对象和 ID Token
    ↓
触发 onAuthStateChanged 监听器
```

### 3. 认证状态监听

```
页面加载
    ↓
Firebase 检查本地存储的 Token
    ↓
如果 Token 有效 → 用户已登录
如果 Token 无效/不存在 → 用户未登录
    ↓
触发 onAuthStateChanged 监听器
    ↓
更新 UI（显示/隐藏登录按钮等）
```

### 4. ID Token

- **什么是 ID Token？**
  - JWT（JSON Web Token）格式
  - 包含用户信息（uid, email 等）
  - 用于验证用户身份

- **Token 的生命周期：**
  - 创建：用户登录时
  - 刷新：自动刷新（约 1 小时）
  - 失效：用户登出或 Token 过期

- **如何使用 Token？**
  - 发送到后端 API 验证用户身份
  - 在后端使用 Firebase Admin SDK 验证 Token

## 🔒 安全最佳实践

1. **密码要求：**
   - 至少 6 个字符（Firebase 默认要求）
   - 建议：包含大小写字母、数字、特殊字符

2. **HTTPS：**
   - 生产环境必须使用 HTTPS
   - Firebase 要求 HTTPS 来保护数据传输

3. **Token 验证：**
   - 在后端验证 ID Token
   - 不要信任前端的认证状态
   - 使用 Firebase Admin SDK 验证 Token

4. **错误处理：**
   - 不要向用户显示详细的错误信息
   - 记录错误日志用于调试
   - 显示友好的错误消息

## 🐛 常见问题

### 1. "Firebase: Error (auth/operation-not-allowed)"

**原因：** 未在 Firebase Console 中启用 Email/Password 登录方式

**解决：** 在 Firebase Console → Authentication → Sign-in method 中启用 Email/Password

### 2. "Firebase: Error (auth/invalid-api-key)"

**原因：** API Key 配置错误

**解决：** 检查 `firebase-config.js` 中的配置是否正确

### 3. "Firebase: Error (auth/network-request-failed)"

**原因：** 网络连接问题

**解决：** 检查网络连接，确保可以访问 Firebase 服务

### 4. 用户登录后立即登出

**原因：** 可能是 Token 刷新失败

**解决：** 检查网络连接，确保 Firebase 服务可访问

## 📚 相关资源

- [Firebase Authentication 文档](https://firebase.google.com/docs/auth)
- [Firebase Authentication Web 指南](https://firebase.google.com/docs/auth/web/start)
- [Firebase 错误代码](https://firebase.google.com/docs/auth/admin/errors)

## 🎯 下一步

1. ✅ 设置 Firebase 项目
2. ✅ 配置认证
3. ✅ 实现登录/注册
4. 🔜 在后端验证 ID Token（可选）
5. 🔜 实现密码重置功能（可选）
6. 🔜 添加社交登录（Google, GitHub 等）（可选）


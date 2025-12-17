/**
 * ============================================
 * Firebase 配置文件
 * ============================================
 * 
 * 这个文件包含 Firebase 的初始化配置
 * 
 * 使用前需要：
 * 1. 在 Firebase Console (https://console.firebase.google.com/) 创建项目
 * 2. 启用 Authentication（认证）服务
 * 3. 启用 Email/Password 登录方式
 * 4. 获取 Web 应用的配置信息（apiKey, authDomain 等）
 * 5. 将配置信息替换到下面的 firebaseConfig 对象中
 * 
 * 如何获取 Firebase 配置：
 * 1. 打开 Firebase Console
 * 2. 选择你的项目
 * 3. 点击项目设置（齿轮图标）
 * 4. 滚动到"你的应用"部分
 * 5. 选择 Web 应用（</> 图标）
 * 6. 复制配置对象
 */

/**
 * Firebase 配置对象
 * 
 * 这个对象包含连接到你的 Firebase 项目所需的所有信息
 * 
 * 注意：这些配置信息是公开的，可以安全地放在前端代码中
 * Firebase 使用安全规则来保护你的数据，而不是隐藏配置信息
 * 
 * 配置项说明：
 * - apiKey: API 密钥，用于标识你的项目
 * - authDomain: 认证域名，用于 Firebase Authentication
 * - projectId: 项目 ID，你的 Firebase 项目的唯一标识
 * - storageBucket: 存储桶，用于 Firebase Storage
 * - messagingSenderId: 消息发送者 ID，用于 Firebase Cloud Messaging
 * - appId: 应用 ID，你的 Web 应用的唯一标识
 */
const firebaseConfig = {
    apiKey: "AIzaSyApP1MYlhPTz_Ugt4c7Z4aa-0bx6jIZoWw",
    authDomain: "math-problem-generator-57a9b.firebaseapp.com",
    projectId: "math-problem-generator-57a9b",
    storageBucket: "math-problem-generator-57a9b.firebasestorage.app",
    messagingSenderId: "297336680236",
    appId: "1:297336680236:web:120a787f127729d1b28689",
    measurementId: "G-WCCGTSJGGV"
};

/**
 * ============================================
 * Firebase 初始化
 * ============================================
 * 
 * 初始化 Firebase 应用
 * 这行代码会创建一个 Firebase 应用实例，连接到你的 Firebase 项目
 */
try {
    // 检查 firebase 是否已加载
    if (typeof firebase === 'undefined') {
        console.error('错误: Firebase SDK 未加载！请检查 script 标签是否正确引入。');
        throw new Error('Firebase SDK 未加载');
    }
    
    console.log('Firebase SDK 已加载，开始初始化...');
    const app = firebase.initializeApp(firebaseConfig);
    console.log('Firebase 初始化成功');
} catch (error) {
    console.error('Firebase 初始化错误:', error);
    console.error('错误详情:', error.message);
    // 不抛出错误，让页面继续加载，错误会在 login.html 中处理
}

/**
 * ============================================
 * Firebase Authentication 服务
 * ============================================
 * 
 * 获取 Firebase Authentication 服务
 * 
 * Firebase Authentication 提供：
 * - 用户注册（createUserWithEmailAndPassword）
 * - 用户登录（signInWithEmailAndPassword）
 * - 用户登出（signOut）
 * - 监听认证状态变化（onAuthStateChanged）
 * - 获取当前用户（currentUser）
 * - 密码重置（sendPasswordResetEmail）
 * - 等等...
 * 
 * 工作原理：
 * 1. 用户注册/登录时，Firebase 会创建一个用户账户
 * 2. Firebase 会返回一个 ID Token（JWT）
 * 3. 这个 Token 可以用来验证用户身份
 * 4. Token 会自动刷新，保持用户登录状态
 * 5. 可以监听认证状态变化，自动更新 UI
 */
try {
    if (typeof firebase !== 'undefined' && firebase.auth) {
        const auth = firebase.auth();
        console.log('Firebase Auth 服务获取成功');
    } else {
        console.error('错误: Firebase Auth 服务不可用');
    }
} catch (error) {
    console.error('获取 Firebase Auth 服务错误:', error);
}

/**
 * ============================================
 * 导出供其他文件使用
 * ============================================
 * 
 * 如果使用模块系统（ES6 modules），可以这样导出：
 * export { auth, app };
 * 
 * 但在这个项目中，我们使用全局变量，所以不需要导出
 * 其他文件可以直接使用 window.auth 或直接使用 auth（如果在全局作用域）
 */


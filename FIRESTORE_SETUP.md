# Firestore 设置指南

本文档说明如何配置 Firebase Firestore 以支持数据存储功能。

## 1. 启用 Firestore

1. 打开 [Firebase Console](https://console.firebase.google.com/)
2. 选择你的项目：`math-problem-generator-57a9b`
3. 在左侧菜单中，点击 **Firestore Database**
4. 点击 **创建数据库**
5. 选择 **以测试模式启动**（稍后配置安全规则）
6. 选择数据库位置（建议选择离你最近的区域）

## 2. 配置安全规则

在 Firestore Console 中，点击 **规则** 标签页，然后粘贴以下规则：

```javascript
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    // 用户偏好 - 只能访问自己的
    match /userPreferences/{userId} {
      allow read, write: if request.auth != null && 
                           request.auth.uid == userId;
    }
    
    // 收藏题目 - 只能访问自己的
    match /favorites/{favoriteId} {
      allow read, write: if request.auth != null && 
                           request.auth.uid == resource.data.userId;
      allow create: if request.auth != null && 
                     request.auth.uid == request.resource.data.userId;
    }
    
    // 保存的 Prompt - 只能访问自己的
    match /savedPrompts/{promptId} {
      allow read, write: if request.auth != null && 
                           request.auth.uid == resource.data.userId;
      allow create: if request.auth != null && 
                     request.auth.uid == request.resource.data.userId;
    }
  }
}
```

点击 **发布** 保存规则。

## 3. 创建索引（如果需要）

如果遇到查询错误，Firebase 会提示你创建索引。按照提示创建即可。

通常需要为以下查询创建索引：
- `favorites` 集合：`userId` (升序) + `createdAt` (降序)
- `savedPrompts` 集合：`userId` (升序) + `createdAt` (降序)

## 4. 数据迁移（可选）

已登录用户的数据会自动从 localStorage 迁移到 Firestore。迁移逻辑在 `index.html` 中实现。

## 5. 数据结构

### userPreferences 集合
```
userPreferences/{userId}
  - question1: string
  - question2: string
  - question3: string
  - updatedAt: timestamp
```

### favorites 集合
```
favorites/{favoriteId}
  - userId: string
  - problem: string
  - hints: string
  - solution: string
  - answer: string
  - problemHash: string
  - title: string
  - createdAt: timestamp
```

### savedPrompts 集合
```
savedPrompts/{promptId}
  - userId: string
  - topic: string
  - grade: string
  - difficulty: string
  - number: string
  - requirements: string
  - selectedTags: array
  - title: string
  - createdAt: timestamp
```

## 6. 测试

1. 登录应用
2. 保存一些数据（收藏题目、保存 Prompt、设置偏好）
3. 在 Firestore Console 中查看数据是否正确保存
4. 登出后，数据应保存在 Firestore（不会丢失）
5. 重新登录，数据应该能正确加载

## 7. 注意事项

- **免费额度**：Firestore 有免费额度，超出后按使用量收费
- **离线支持**：Firestore 支持离线缓存，但需要配置
- **实时同步**：数据变化会自动同步到所有设备
- **降级处理**：如果 Firestore 操作失败，会自动降级到 localStorage

## 8. 故障排除

### 问题：数据没有保存到 Firestore

**检查**：
1. 用户是否已登录？
2. Firestore 是否已启用？
3. 安全规则是否正确配置？
4. 浏览器控制台是否有错误？

### 问题：查询失败

**检查**：
1. 是否创建了必要的索引？
2. 安全规则是否允许查询？
3. 查询条件是否正确？

### 问题：权限错误

**检查**：
1. 安全规则中的 `request.auth.uid` 是否正确？
2. 用户是否已登录？
3. 数据中的 `userId` 字段是否正确设置？


# API密钥设置指南

## 环境变量设置

本项目使用环境变量来存储和访问API密钥，避免将敏感信息硬编码在代码中。请按照以下步骤设置所需的环境变量。

**注意：** 当前系统设计中，BigModel、ChatGPT和Coze这三个模型的后端是独立的，每次只能配置一个模型使用。根据您想要使用的模型，设置相应的环境变量。

### 本地开发环境设置

#### Windows环境

在命令提示符中设置临时环境变量：
```
rem 使用智谱大模型(BigModel)
set API_KEY=your_zhipu_glm_api_key

rem 或者使用OpenAI(ChatGPT)
set API_KEY=your_openai_api_key

rem 或者使用Coze
set API_KEY=your_coze_api_token
set COZE_BOT_ID=your_coze_bot_id
```

在PowerShell中设置临时环境变量：
```
# 使用智谱大模型(BigModel)
$env:API_KEY = "your_zhipu_glm_api_key"

# 或者使用OpenAI(ChatGPT)
$env:API_KEY = "your_openai_api_key"

# 或者使用Coze
$env:API_KEY = "your_coze_api_token"
$env:COZE_BOT_ID = "your_coze_bot_id"
```

或者设置永久环境变量：
1. 右键点击"此电脑"→"属性"→"高级系统设置"→"环境变量"
2. 在"用户变量"部分点击"新建"，添加上述变量和对应的值

#### Linux/MacOS环境

在终端中设置临时环境变量：
```bash
# 使用智谱大模型(BigModel)
export API_KEY=your_zhipu_glm_api_key

# 或者使用OpenAI(ChatGPT)
export API_KEY=your_openai_api_key

# 或者使用Coze
export API_KEY=your_coze_api_token
export COZE_BOT_ID=your_coze_bot_id
```

永久设置：将上述命令添加到`~/.bashrc`或`~/.zshrc`文件中

### 部署环境设置

#### Render

1. 在Render控制台中，选择您的Web服务
2. 转到"Environment"部分
3. 根据您选择使用的模型添加相应的环境变量：
   - 智谱大模型：`API_KEY`
   - OpenAI：`API_KEY`
   - Coze：`API_KEY`和`COZE_BOT_ID`

#### 其他云平台

大多数云平台都提供设置环境变量的方式，请参考相应平台的文档。

## 安全提示

- 永远不要将API密钥提交到版本控制系统中
- 定期轮换API密钥以提高安全性
- 使用最小权限原则，确保API密钥只有必要的访问权限
- 设置API密钥使用限制和监控以防滥用 
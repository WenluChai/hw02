我完成了 Python 版 Chatbot 的代码编写，实现了以下功能：
 网络请求：使用 requests 库构建 HTTPS 请求，鉴权方式为 Bearer Token。
 参数配置：封装了 API_KEY、BASE_URL、MODEL_ID 三个核心配置项。
 交互逻辑：提供 你： / AI： 的命令行交互界面，支持输入 quit 退出。
4. 运行环境与依赖
• Python 版本：3.6+
• 第三方库：request
◦ 安装命令：pip install requests
• 网络环境：需能够正常访问 ark.cn-beijing.volces.com
5. 遇到的问题与解决方案
在调试过程中出现了 400 Bad Request 错误，报错信息为 Mismatch type []*responses.InputItem。
• 原因分析：火山方舟 v3/responses 接口对 input 参数的类型校验极其严格，要求必须是 Array（数组）类型，而不是 Object（对象）。
• 修正方案：将数据结构中 input 字段的格式从嵌套字典 {"messages": [...]} 调整为直接传入数组 [...]，完美解决参数不匹配问题。
注意事项
1. 隐私安全：切勿将真实 API_KEY 上传至公开仓库，提交时需替换为占位符（如 "你的Bearer Token"）
2. 接口格式：严格遵循火山方舟 v3 接口规范，input 参数需为数组格式 [{"role": "user", "content": "问题"}]
3. 网络要求：需确保能正常访问 ark.cn-beijing.volces.com，校园网环境可能需要切换热点
4. 异常处理：代码已包含状态码捕获与错误提示，若出现 400/401 错误，需检查 API_KEY 或接口格式

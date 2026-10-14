# LX-AICODING Course Backend

Windows 本地运行版 AI Coding 教学项目。
参考项目：见LX_AICoding\docs\reviewer_references\open_source_reviewer_comparison.md
## 1. Alibaba open-code-review -- https://github.com/alibaba/open-code-review
## 2. serge
## 3. Robin
## 4. Vercel OpenReview
## 5. Dailybot AI Diff Reviewer
## 6. 对 LX-AICODING 第一版的取舍结论


课程方案文档：
```text
docs\LX_AICODING_COURSE_REBUILD_PLAN.md ----\LX_AICoding\docs\LX_AICODING_COURSE_REBUILD_PLAN.md
```


## 启动
项目配置文件：
```text
.env
```
如果本项目 `.env` 中填写了同名变量，本项目配置优先。


启动后端：
```powershell
scripts\start_backend.cmd
```


启动前端：
```powershell
scripts\start_ui.cmd
```


同时启动前后端：
```powershell
.venv\Scripts\python.exe scripts\start_all.py
```


打开：
```text
http://127.0.0.1:2024/health
http://127.0.0.1:3000/agents
```
后端通过 FastAPI/Uvicorn 运行，不使用 `langgraph dev`。##===================================##===================================




## 前后端交互
当前前端采用 Vue + POST SSE 方式和后端交互，，不再使用旧版 `/api/tasks` 后台任务接口。
前端实际调用的 Dashboard API：
```text
GET    /dashboard/api/me
GET    /dashboard/api/options
GET    /dashboard/api/threads
GET    /dashboard/api/threads/{thread_id}
POST   /dashboard/api/threads/stream-message
POST   /dashboard/api/threads/{thread_id}/stream-message
DELETE /dashboard/api/threads/{thread_id}
```

后端会在同一个流式响应中 依次返回用户消息、任务计划和 AI 输出。




## 数据文件
```text
data\checkpoints.sqlite ，保存聊天历史和 thread state   ，，见graph.py的- Checkpoint 面向 Agent 的 thread state 和消息历史恢复。 负责保存 Agent 运行过程中的 messages、工具调用状态和 thread state。
LangGraph checkpoint，，见graph.py的 - Store 面向页面和业务查询。
data\store.sqlite        业务Store，保存任务摘要、PR URL、review findings，，见graph.py的 - ##专门服务 `/memories/...` 长期记忆文件 
```
前端历史记录只从 checkpoint 恢复；
Store 不参与前端聊天正文展示。




## 日志文件
```text
logs\backend-YYYY-MM-DD.log      FastAPI、接口、配置和异常日志
logs\agent-runs-YYYY-MM-DD.log   Agent 任务运行日志，包括 clone、测试、push、PR 等步骤
```
严格清理旧前端不用的接口后，浏览器日志读取接口 `/api/logs/backend` 和 `/api/logs/agent` 已删除。
需要排查日志时，直接查看项目 `logs` 目录。




## 验证
基础后端验证，不会调用模型或 push：
```powershell
.venv\Scripts\python.exe scripts\verify_backend.py
```

真实 Gitee 端到端验证会调用模型并创建 PR，请只对测试仓库运行：
```powershell
.venv\Scripts\python.exe scripts\verify_gitee_e2e.py https://gitee.com/owner/repo.git
```
当前真实验收仓库：
```text
https://gitee.com/msb-goldbin/ai_coding
```


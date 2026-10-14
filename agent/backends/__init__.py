"""Agent 后端能力包。

这个目录是 LX-AICODING 中 Coding Agent 能够“真正操作代码”的底座。

各文件职责：
- `local_shell.py`：实现 DeepAgents 本地 Windows backend，负责
          文件读写、
          命令执行、
          Gitee Git 认证、
          虚拟路径映射
          和安全边界。
- `workspace.py`：封装工作区根目录和路径解析，保证所有相对路径最终都落在工作区内。
- `permissions.py`：提供更底层的路径、命令、Git分支名和提交信息安全校验。

讲课时要强调：
Prompt只能告诉模型“应该怎么做”，但backend才决定模型“实际能做什么”。
这个包里的代码就是 Agent写代码、读文件、执行命令时的最后一道工程边界。
"""

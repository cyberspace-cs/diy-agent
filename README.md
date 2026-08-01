# diy-agent-demo1

> 从零动手实现一个 LLM Agent 的 7 天学习实践项目。

本项目是我在学习 [`kris330/my-first-agent`](https://github.com/kris330/my-first-agent) 课程仓库基础上，**按自己的理解和环境重构、本地化、并补充中文注释**的版本。代码按 `day1` ~ `day7` 分目录组织，每天对应课程的一个里程碑。
这是对应的微信文章：[Day 7：完整项目收尾——整合、部署、下一步]
(https://mp.weixin.qq.com/s/qIW5QKdY_TnAWW-vYZRjbg)

---

## 与 kris330/my-first-agent 的区别

本项目**不是**原仓库的 fork，而是基于其课程大纲的**二次实践**。主要差异如下：

| 维度 | kris330/my-first-agent（原项目） | 本项目 diy-agent-demo1 |
| --- | --- | --- |
| 定位 | 完整课程仓库（含 final_project、multi_agent、docs 等） | 聚焦**核心 7 天 Agent 实现**的学习笔记与可运行代码 |
| 目录结构 | 按课程模块组织，含 `final_project/`、`multi_agent/`、`docs/` | 仅保留 `day1` ~ `day7`，结构更精简、聚焦主线 |
| LLM 接入 | 默认走 OpenAI 官方接口 | 适配**国内可用**的 OpenAI 兼容服务（如 DeepSeek），通过 `.env` 的 `OPENAI_BASE_URL` / `OPENAI_MODEL` 切换 |
| 环境变量 | 根目录统一 `.env.example` | 每个 day 目录独立 `.env`（本地），并提供根目录统一 `.env.example` 模板 |
| 代码注释 | 英文、偏教学描述 | 增加**中文注释**与本地化说明，便于自己回顾 |
| 敏感信息 | 已用 `.env.example` 脱敏 | 严格忽略 `.env`（见下方说明），仅上传 `.env.example` |

### 本项目**没有**包含原仓库的哪些部分
- `final_project/`（综合项目）、`multi_agent/`（多智能体进阶）、`docs/`（课程文档）等扩展内容。
- 这些是原课程的后续章节，等我把 day1-day7 主线吃透后会单独开仓库或分支继续。

### 本项目**额外**做了什么
- 适配国内 LLM 服务（DeepSeek 等兼容 OpenAI 协议的服务）。
- 统一依赖清单 `requirements.txt`。
- 完善 `.gitignore`，确保含 API Key 的 `.env` 永不入库。

---

## 项目结构

```
diy-agent-demo1/
├── README.md                 # 本文件
├── requirements.txt          # Python 依赖
├── .env.example              # 环境变量模板（复制为 .env 后填写）
├── .gitignore                # 忽略 .env / __pycache__ 等
├── day1/                     # 体验 LLM：直接调用对话接口
├── day2/                     # 第一个 Agent：系统提示 + 工具注册 + JSON 决策
├── day3/                     # 增强工具调用：天气等真实工具
├── day4/                     # 多轮对话 / 上下文管理
├── day5/                     # 记忆机制（短期/长期）
├── day6/                     # 规划与反思（ReAct 思路）
└── day7/                     # 综合：本地运行一个较完整的 Agent
```

---

## 快速开始

### 1. 安装依赖
```bash
pip install -r requirements.txt
```

### 2. 配置环境变量
每个 `day` 目录需要一个 `.env` 文件（已本地存在，不会上传）。若从零部署，复制模板即可：
```bash
cp .env.example day1/.env
# 然后编辑 day1/.env，填入你的 API Key
```
> `.env` 文件包含敏感信息，**已被 `.gitignore` 忽略，不会上传到 GitHub**。请只提交/分享 `.env.example`。

`.env` 字段说明：
| 变量 | 说明 | 示例 |
| --- | --- | --- |
| `OPENAI_API_KEY` | LLM 服务的 API Key（必填） | `sk-xxxx` |
| `OPENAI_BASE_URL` | 接口地址，国内服务填对应地址 | `https://api.deepseek.com` |
| `OPENAI_MODEL` | 模型名 | `deepseek-v4-flash` |
| `BAIDU_API_KEY` | 百度天气等工具所需 Key（可选） | `xxxx` |

### 3. 运行
进入对应 day 目录，按各目录内的说明或入口脚本运行，例如：
```bash
cd day1
python main.py
```

---

## 同步说明（给未来的自己）
- 远程仓库：`https://github.com/cyberspace-cs/diy-agent.git`，默认分支 `main`。
- 本机推送走 **HTTPS + 本地 7897 代理**（不要用 SSH/SOCKS5 转发，会卡死）。
- 日常改动后：`git add . && git commit -m "..." && git push`。
- **切勿提交 `.env`**；敏感 Key 只留在本地。

---

## 致谢
课程大纲与思路参考自 [kris330/my-first-agent](https://github.com/kris330/my-first-agent)，感谢原作者。本仓库为其学习实践重构版。

## 参考文章
- [Day 7：完整项目收尾——整合、部署、下一步](https://mp.weixin.qq.com/s/qIW5QKdY_TnAWW-vYZRjbg)

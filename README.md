# ThoughtAdvisor

ThoughtAdvisor - 06-思想-Thought 行业 Web 项目

## 项目说明
基于张勇的 36 行业架构,ThoughtAdvisor 是 思想-Thought 行业的 Web 端顾问产品。
完整规划见 [`项目开发计划.md`](项目开发计划.md)(简化版)与 [`思想顾问开发架构与计划.md`](思想顾问开发架构与计划.md)(详设版)。

## 行业分工定位(36 行业 · 思想 vs 智库 vs 演讲 vs 其他)

| 行业 | 内部代号 | Web 项目目录 | 核心产物 | 与思想行业的关系 |
|------|---------|-------------|---------|----------------|
| **思想·Thought**(本项目) | 06-思想 | `_ThoughtLib/ThoughtWeb/` | 思想图谱 + 经典导读 + 议题梳理 | **知识源** — 长期沉淀东西方哲学骨架 |
| 智库·ThinkTank | 05-智库 | `_ThinkTankLib/ThinkTankWeb/` | 行业研究 + 战略咨询 | **应用层** — 引用思想行业骨架做现实映射 |
| 演讲·Speech | 00-演讲 | `00_Speech/`(非 Web) | 演讲稿 + Skill 模板 | **表达层** — 借用思想行业典故作素材 |
| 其他 33 行业 | 07~36 | 各 `_XxxLib/XxxWeb/` | 各自行业顾问 | **横向引用** — 思想行业作为元叙事底座 |

> **思想行业定位**:**知识底座** + **元叙事**。
> 不直接做商业咨询(那是智库),不直接写演讲稿(那是演讲),
> 而是给所有行业提供"思想史 / 哲学骨架 / 经典原文" 的可引用底层。
> 飞书 Bot 已上线(随问随答),Web 端 MVP 当前阶段为骨架起步。

## 快速开始

```bash
# 安装依赖(Phase 1 MVP 起步 3 项)
pip install -r requirements.txt

# 启动 FastAPI hello world
uvicorn src.main:app --reload --port 8006

# 访问
open http://127.0.0.1:8006/
```

## 数据资产(`data/`)

| 文件 | 内容 | 进度 |
|------|------|------|
| `topics_index.json` | 10 大主题索引 | ✅ 100% |
| `thinkers_v1.json` | 思想家种子 | 🟡 14/100 |
| `classics_v1.json` | 经典种子 | 🟡 19/50 |
| `graph_schema_v1.json` | 思想图谱 schema | 🟡 5 节点 + 6 关系 |
| `issue_framework_v1.json` | 议题梳理框架 | 🟡 3/50 |

## 同步
- GitHub: https://github.com/1500385678/ThoughtAdvisor
- Gitee:  https://gitee.com/architectzy/ThoughtAdvisor

## 自动化
- T4 每日 02:00 检查项目并更新开发计划
- T5 每日 03:50 完成小步开发并 commit + push

"""ThoughtAdvisor · 思想顾问 Web 端核心代码

Phase 1 MVP 起步件 · 2026-09-10 T5 兜底

服务模块拆分(规划):
  - src/api/     FastAPI 路由层 (/map /guide /issue /text /read)
  - src/services/ 业务服务层(图谱/导读/议题/精读/AI 哲学引擎)
  - src/data/    数据访问层(SQLite → PostgreSQL+Neo4j)
  - src/schemas/ Pydantic 模型
"""

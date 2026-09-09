"""ThoughtAdvisor · FastAPI 入口 · Phase 1 MVP 起步件

T5 兜底 2026-09-10:从 0 → 1 hello world,触发"失能期最低存活动作"链路。
Phase 0 知识库见 ../data/(topics_index / thinkers_v1 / classics_v1 /
graph_schema_v1 / issue_framework_v1),Phase 1 起先把 FastAPI 跑通,
再接 /map /guide /issue /text /read 五个核心接口。
"""
from fastapi import FastAPI

app = FastAPI(
    title="ThoughtAdvisor",
    description="06-思想-Thought 行业 Web 端 · 思想史顾问",
    version="0.1.0",
)


@app.get("/")
async def root() -> dict[str, str]:
    return {
        "project": "ThoughtAdvisor",
        "industry": "06-思想-Thought",
        "phase": "1-MVP-starting",
        "hello": "世界",
    }


@app.get("/healthz")
async def healthz() -> dict[str, str]:
    return {"status": "ok"}

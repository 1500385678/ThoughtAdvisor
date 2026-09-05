# 思想图谱 Schema v1.0

> 阶段:Phase 0 任务 4 · 图谱 schema 冻结
> 生成日期:2026-09-06
> 状态:**frozen** — 字段冻结,实例填充延至 Phase 0 任务 5/6
> 兜底来源:0902 plan P3 建议(0903 必启图谱 schema v1,延至 0906 启动)

---

## 一、设计原则

1. **软关联优先**:节点之间通过 `id` 字符串软关联,不强外键,便于单独迭代 topics / thinkers / classics 三个数据文件
2. **字段对齐**:与 `topics_index.json v1.0` / `thinkers_v1.json v1.0` / `classics_v1.json v1.0` 字段同构,id 命名一致(`T<两位数>` / `C<两位数>` / 主题两位数)
3. **延后硬外键**:Neo4j 硬外键 + 双向索引延至 Phase 1 MVP,本任务只冻结 schema
4. **可演化**:5 节点 + 6 关系基本覆盖思想史图谱所有典型关系,新需求先尝试落在现有节点/边上,新增类型需走 schema 升级流程

---

## 二、5 个节点类型

| 节点 | id 模式 | 字段(节选) | 数据来源 | 状态 |
|------|---------|------------|----------|------|
| **thinker** 思想家 | `T<两位数>` 例:T01 | id / name_cn / name_en / birth_year / death_year / topic_id / school / brief / one_liner / key_works[classic_ids] / representative_quotes[] / source_path | `data/thinkers_v1.json v1.0` | ✅ 已入机 13 人物 |
| **school** 学派/流派 | `S<两位数>` 例:S01 | id / name_cn / name_en / topic_id / founder_ids[thinker_ids] / core_ideas[] / era / brief / source_path | 待 Phase 0 任务 5 | ⏳ schema 冻结,实例待启 |
| **classic** 经典文本 | `C<两位数>` 例:C01 | id / title_cn / title_en / author_ids[thinker_ids] / era / school / topic_id / brief / one_liner / representative_chapters[] / source_path | `data/classics_v1.json v1.0` | ✅ 已入机 10 经典 |
| **idea** 核心命题 | `I<两位数>` 例:I01 | id / name / topic_id / proposer_ids[thinker_ids] / classic_ids[classic_ids] / school_ids[school_ids] / one_liner / keywords[] / counter_idea_ids[] | 待 Phase 0 任务 5 | ⏳ schema 冻结,实例待启 |
| **era** 时代/时期 | `E<两位数>` 例:E01 | id / name / start_year / end_year / topic_ids[topic_ids] / representative_thinker_ids[thinker_ids] / brief | 待 Phase 0 任务 5 | ⏳ schema 冻结,实例待启 |

**软关联约定**:所有 `*_ids` 字段统一为数组(thinker_ids / classic_ids / school_ids / idea_ids / era_ids / topic_ids),与 `classics_v1.author_ids` 数组化保持一致。

---

## 三、6 个关系类型

| 关系 | 起点 | 终点 | 字段(节选) | 示例 |
|------|------|------|------------|------|
| **belongs_to** 归属于 | thinker / classic / idea | school / topic / era | weight(0-1) / primary(bool) | T03 王阳明 -[belongs_to]-> S01 心学(weight=1.0, primary=true) |
| **wrote** 著有/撰写 | thinker | classic | role(author/editor/co-author) / year | T01 毛泽东 -[wrote]-> C01 矛盾论(role=author, year=1937) |
| **influenced** 影响 | thinker / classic / idea / school | thinker / classic / idea / school | weight(0-1) / direction(direct/indirect) / note | (实例待 Phase 0 任务 6) |
| **criticized** 批评/反驳 | thinker / classic / idea | thinker / classic / idea / school | weight(0-1) / stance(refute/revise/extend) / note | T01 毛泽东 -[criticized]-> 教条主义(stance=refute) |
| **contemporary_with** 同时代 | thinker | thinker | era_overlap_years / geography(same/cross-region) | T07 庄子 -[contemporary_with]-> 惠子(era_overlap_years≈30) |
| **branch_of** 分支自/师承 | school / thinker | school / thinker | relation(master/apprentice/branch) / year | S01 心学 -[branch_of]-> 理学(relation=revise) |

---

## 四、字段对齐矩阵(与现有数据)

| 字段 | topics_index | thinkers_v1 | classics_v1 | graph schema |
|------|--------------|-------------|-------------|--------------|
| `id` 命名 | `01` (主题两位) | `T01` | `C01` | thinker `T01` / school `S01` / classic `C01` / idea `I01` / era `E01` |
| `topic_id` 软关联 | 主键 | 外键(主题) | 外键(主题) | 外键(主题) |
| `author_ids` 数组 | n/a | n/a | `["T01"]` | `thinker_ids` 数组 |
| `brief` 简介 | 有 | 有 | 有 | thinker / classic / school / era 都有 |
| `one_liner` 一句话 | n/a | 有 | 有 | thinker / classic / idea 都有 |
| `source_path` 库路径 | n/a | 有 | 有 | thinker / classic / school 都有 |

**id 同号不同名空间**:`01` 是主题 id,`T01`/`C01`/`S01`/`I01`/`E01` 是不同节点 id,字符串不相同不冲突,主题 id 作为 topic_id 软关联到其他节点。

---

## 五、扩展计划

| 阶段 | 任务 | 工作 |
|------|------|------|
| Phase 0 任务 5 | school/idea/era 三库启动 | 按本 schema 字段填实例(目标:school 10+/ idea 30+/ era 8+) |
| Phase 0 任务 6 | influenced/criticized/contemporary_with 三类边 | 沿 0902 兜底 P2 建议,实例填充(目标:边 50+) |
| Phase 1 MVP | Neo4j 硬外键迁移 | 本 schema 字段保持不变,只做实体化 + 双向索引 |

---

## 六、不做什么(本任务边界)

- ❌ 不填任何节点/边的实例数据(本任务仅冻结 schema,实例归 Phase 0 任务 5/6)
- ❌ 不改 `topics_index.json` / `thinkers_v1.json` / `classics_v1.json`(沿 0902 原则,只冻结 schema 不动现有数据)
- ❌ 不实施 Neo4j 硬外键 + 双向索引(Phase 1 MVP 范围)
- ❌ 不勾选 `项目开发计划.md` 任务 4 checkbox(实例未填,沿 0826 原则整体收尾时统一勾选)

---

## 七、关联文档

- [topics_index.json](topics_index.json) v1.0 — 10 主题(2026-08-26)
- [topics_index.md](topics_index.md) v1.0
- [thinkers_v1.json](thinkers_v1.json) v1.0 — 13 人物(2026-08-29)
- [thinkers_v1.md](thinkers_v1.md) v1.0
- [classics_v1.json](classics_v1.json) v1.0 — 10 经典(2026-09-02)
- [classics_v1.md](classics_v1.md) v1.0
- [项目开发计划.md](../项目开发计划.md) Phase 0 任务 4

---

## 八、变更记录

- **2026-09-06** v1.0 frozen — Phase 0 任务 4 启动,5 节点 + 6 关系 schema 冻结,实例填充延至 Phase 0 任务 5/6;0902 兜底 P3 建议落地(延迟 3 天)

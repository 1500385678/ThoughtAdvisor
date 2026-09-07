# 议题框架 · issue_framework_v1

> 机器索引:`data/issue_framework_v1.json` · schema_version 1.0 · generated 2026-09-08
> 来源:`data/thinkers_v1.json v1.0` + `data/classics_v1.json v1.0` + `data/topics_index.json v1.0`
> 用途:Phase 0 任务 5 的种子表,作为图谱应用层(议题梳理)的入口结构;后续每日 1-2 议题扩展至 50

---

## 设计原则

1. **软关联优先**:`topic_ids[]` / `classic_ids[]` 数组化,不强外键,便于单独迭代 topics / thinkers / classics / issues 四个数据文件
2. **字段对齐**:与 `topics_index.json v1.0` / `thinkers_v1.json v1.0` / `classics_v1.json v1.0` / `graph_schema_v1.json v1.0` 字段同构,`thinker_id` 命名一致(`T<两位数>`),`classic_id` 命名一致(`C<两位数>`),`topic_id` 软关联到 `topics_index`
3. **一对多立场**:`positions[]` 数组支持同一议题多个立场(本次每议题 2 立场,典型对比场景)
4. **多形态分类**:`category` 枚举(认识论 / 方法论 / 价值观 / 本体论 / 伦理学 / 政治哲学 / 美学),便于按形态分布统计
5. **可演化**:本 schema 覆盖思想史典型议题所有必要字段,新需求先尝试落在现有字段,新增枚举/字段需走 schema 升级流程

---

## 总览(3 议题)

| 议题 ID | 议题(中文) | 类别 | 主题 | 立场数 | 关键人物 |
|---------|-----------|------|------|--------|----------|
| I01 | 知与行,孰先孰后? | 认识论 | 03 / 01 | 2 | T03 王阳明 / T01 毛泽东 |
| I02 | 改革应解放思想还是实事求是? | 方法论 | 02 / 01 | 2 | T02 邓小平 / T01 毛泽东 |
| I03 | 处世应兼爱济世还是逍遥超脱? | 价值观 | 06 / 07 | 2 | T06 墨子 / T07 庄子 |

合计 3 议题 / 5 主题 / 3 形态 / 5 立场(每位人物可能出现在多个议题)。

---

## 主题分布(3 议题)

| 主题 | 议题数 | 议题 ID |
|------|--------|---------|
| 01 毛泽东思想 | 2 | I01, I02 |
| 02 邓小平理论 | 1 | I02 |
| 03 王阳明心学 | 1 | I01 |
| 06 墨子思想 | 1 | I03 |
| 07 庄子思想 | 1 | I03 |
| 04 / 05 / 08 / 09 / 10 | 0 | (待补) |

合计 5 主题有议题,5 主题(04 / 05 / 08 / 09 / 10)待补。

---

## 形态分布(3 议题)

| 类别 | 议题数 | 议题 ID |
|------|--------|---------|
| 认识论 | 1 | I01 |
| 方法论 | 1 | I02 |
| 价值观 | 1 | I03 |
| 本体论 / 伦理学 / 政治哲学 / 美学 | 0 | (待补) |

合计 3 形态已覆盖,4 形态待补。

---

## 立场表(3 议题 / 6 立场)

| 议题 | 立场 | 思想家 | 学派 | 关键引文 | 经典引用 |
|------|------|--------|------|----------|----------|
| I01 | 知行合一 | T03 | 心学 | 知是行的主意,行是知的功夫;知而不行,只是未知 | C03 传习录 |
| I01 | 行先知后 | T01 | 实践论 | 通过实践而发现真理,又通过实践而证实真理和发展真理 | C02 实践论 |
| I02 | 解放思想先行 | T02 | 改革开放 | 解放思想,开动脑筋,实事求是 | (02 主题经典待补) |
| I02 | 实事求是是根本 | T01 | 矛盾论 | "实事"就是客观存在着的一切事物,"是"就是客观事物的内部联系 | C01 矛盾论 / C02 实践论 |
| I03 | 兼爱非攻 | T06 | 墨家 | 兼相爱,交相利 | (06 主题经典待补) |
| I03 | 逍遥无为 | T07 | 道家 | 若夫乘天地之正,而御六气之辩,以游无穷者,彼且恶乎待哉 | C06 庄子 |

合计 6 立场 / 5 人物(T01 在 2 议题出现,其余各 1 议题)。

---

## 字段说明

| 字段 | 类型 | 说明 | 示例 |
|------|------|------|------|
| `issue_id` | string | 议题 id,`I<两位数>` 模式 | `I01` |
| `question_cn` | string | 议题中文 | `知与行,孰先孰后?` |
| `question_en` | string | 议题英文 | `Which comes first: knowledge or action?` |
| `topic_ids` | string[] | 涉及主题 id 数组(软关联 `topics_index`) | `["03", "01"]` |
| `category` | string | 议题类别枚举 | `认识论` / `方法论` / `价值观` |
| `one_liner` | string | 议题一句话核心 | `心学主张知行合一不可分...` |
| `positions[]` | object[] | 立场数组,每立场对应一位/一派思想家 | (见下) |
| `positions[].thinker_id` | string | 该立场核心人物 id(关联 `thinkers_v1`) | `T03` |
| `positions[].school` | string | 该立场所属学派 | `心学` / `墨家` |
| `positions[].stance` | string | 该立场一句话概括 | `知行合一` / `兼爱非攻` |
| `positions[].one_liner` | string | 该立场的展开说明 | `知是行之始,行是知之成...` |
| `positions[].key_quote` | string | 该立场代表性引文 | `知是行的主意...` |
| `positions[].classic_ids` | string[] | 该立场涉及的经典 id 数组(关联 `classics_v1`,可空) | `["C03"]` |

**软关联约定**:所有 `*_ids` 字段统一为数组,与 `classics_v1.author_ids` / `graph_schema_v1.thinker_ids` 数组化保持一致。

---

## 扩展计划

- **D+1(0909)**:补 2 议题(目标 5/50)
  - I04 自由意志 vs 必然(主题 10 马克思主义 + 主题 09 卢梭待入机,主题 10 可立即落)
  - I05 礼法 vs 法治(主题 06 墨子 + 主题 09 韩非子待入机,主题 06 可立即落)
- **D+7(0915)**:补 8 议题(目标 11/50,覆盖 04 / 05 / 08 / 09 主题)
- **D+20(0928)**:补 30 议题(目标 33/50,基本覆盖十大主题)
- **D+30(1008)**:补 50 议题(目标 50+,达 Phase 0 任务 5 验收)
- 字段冻结:`schema_version 1.0`,扩展仅在 `issues[]` 数组追加,不动既有字段;`category` 枚举按需新增但需在变更记录中说明

---

## 不做什么(本任务边界)

- ❌ 不填任何议题实例(本次只填 3 议题种子;0909 起每日 1-2 议题扩展)
- ❌ 不改 `topics_index.json` / `thinkers_v1.json` / `classics_v1.json` / `graph_schema_v1.json`(沿 0902 + 0906 原则,只冻结任务 5 schema 不动现有数据)
- ❌ 不勾选 `项目开发计划.md` 任务 5 checkbox(3/50 未达验收,沿 0902 原则"未达验收不勾选")
- ❌ 不实现 LLM 调用 / RAG / 议题对比表 UI(Phase 1 MVP 范围,本任务只落 schema)
- ❌ 不启动 Phase 0 任务 6(SQLite→PostgreSQL+Neo4j 迁移脚本)— 留 0909 单独 T5 兜底
- ❌ 不补经典 2 本(0908 巡检 P0 优先级 1 也建议,留 0909 单独 T5 兜底,避免 1 天塞 2 个 Phase 0 任务)

---

## 关联文档

- [topics_index.json](topics_index.json) v1.0 — 10 主题(2026-08-26)
- [topics_index.md](topics_index.md) v1.0
- [thinkers_v1.json](thinkers_v1.json) v1.0 — 13 人物(2026-08-29)
- [thinkers_v1.md](thinkers_v1.md) v1.0
- [classics_v1.json](classics_v1.json) v1.0 — 10 经典(2026-09-02)
- [classics_v1.md](classics_v1.md) v1.0
- [graph_schema_v1.json](graph_schema_v1.json) v1.0 — 5 节点 + 6 关系(2026-09-06)
- [graph_schema_v1.md](graph_schema_v1.md) v1.0
- [项目开发计划.md](../项目开发计划.md) Phase 0 任务 5

---

## 变更记录

- **2026-09-08** v1.0 frozen — Phase 0 任务 5 启动,3 议题(2 立场/议题)入机,`{issue_id, question_cn, question_en, topic_ids[], category, one_liner, positions[]}` 字段冻结,`positions[].{thinker_id, school, stance, one_liner, key_quote, classic_ids[]}` 子字段冻结;0908 T5 兜底(T4 10 天未落 plan,0902 巡检 P0 优先级 1 任务 5 建议 0908 内启动;本任务只冻结 schema + 3 议题种子,不勾选项目开发计划任务 5 checkbox)

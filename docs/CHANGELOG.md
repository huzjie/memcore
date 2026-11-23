# Changelog

## [1.0.0] - 2026-11-23

- 快慢记忆双通道：WorkingMemory + LongTermMemory。
- 写入门控：importance / salience / novelty 组合打分。
- 混合检索：BM25 + TF-IDF + 时间衰减 + 重要性。
- 记忆巩固：聚簇 → 去重 → 总结。
- 遗忘淘汰：预算 + 指数衰减 + LRU。
- 存储后端：内存 / JSON / SQLite。
- LLM 适配：确定性 mock / OpenAI 兼容。
- 评测：recall@k / MRR / 保留率。
- HTTP 服务、CLI、Docker / Compose / Helm / K8s / CI。

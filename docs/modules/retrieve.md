# 混合检索
`Searcher` 用 BM25+TF-IDF 召回相关性，`HybridScorer` 融合时间 / 重要性，
`recency` 提供指数时间衰减。
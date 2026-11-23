# 调参指南

## 写入门控

| 参数 | 默认 | 影响 |
|---|---|---|
| `gate.threshold` | 0.45 | 越高越严格，记忆越少越精 |
| `gate.weights` | (0.40, 0.35, 0.25) | importance / salience / novelty 权重 |

## 检索

| 参数 | 默认 | 影响 |
|---|---|---|
| `relevance_weight` | 1.0 | 语义相关权重 |
| `recency_bias` | 0.5 | 时间衰减权重 |
| `importance_weight` | 0.5 | 重要性权重 |

## 遗忘 / 巩固

| 参数 | 默认 | 影响 |
|---|---|---|
| `forget.max_items` | 10000 | 超过触发预算淘汰 |
| `consolidate.min_items` | 64 | 达到即触发巩固 |
| `consolidate.cluster_threshold` | 0.70 | 聚簇相似度阈值 |

## 场景建议

- 个人助理（重偏好）：提高 importance 权重、降低 threshold。
- 知识库（重检索）：提高 relevance_weight，用 sqlite store。
- 高并发（重性能）：memory store + 关闭巩固。

# 基准结果

内置 `eval` 基准（8 条事实 + 4 组查询，零依赖 mock）：

```json
{
  "n_items": 8,
  "n_queries": 4,
  "recall@5": 1.0,
  "mrr": 1.0,
  "retention": 1.0
}
```

跑法：`python -m memcore eval`。该口径完全确定性，可在 CI 复现。

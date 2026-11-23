# API 参考

## Memory（门面）

| 方法 | 说明 |
|---|---|
| `add(content, role, scope, tags, force, metadata)` | 写入长期记忆（门控通过才写） |
| `search(query, limit)` | 混合检索，返回 `MemoryResult` 列表 |
| `get(item_id)` / `delete(item_id)` | 读 / 删单条 |
| `all()` / `count()` | 全量 / 计数 |
| `consolidate()` | 巩固长期记忆 |
| `forget()` | 遗忘淘汰 |
| `remember_now(content)` | 写入快记忆 |
| `stats()` | 统计信息 |

## HTTP 端点

- `GET /health` — 健康检查。
- `POST /v1/memories` — `{"content": "...", "force": false}`。
- `POST /v1/memories/search` — `{"query": "...", "limit": 5}`。

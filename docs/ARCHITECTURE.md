# 架构

memcore 采用「快慢记忆」双通道架构，分 10 个松耦合子包。

## 数据流

```
输入内容
   │
   ├─> 快记忆 WorkingMemory（环形缓冲，会话内）
   │
   └─> 写入门控 WriteGate（重要性/显著性/新颖性打分）
          │ 通过阈值
          ▼
     长期记忆 LongTermMemory ── store（内存/JSON/SQLite）
          │
          ├─ 检索 Searcher（相关性+时间+重要性）
          ├─ 巩固 consolidate（聚簇→去重→总结）
          └─ 遗忘 Evictor（预算+衰减）
```

## 分层

- **core**：数据模型（MemoryItem/MemoryQuery/MemoryResult）与 Memory 门面。
- **fast / slow**：快慢记忆两通道。
- **write**：写入门控策略。
- **retrieve**：混合检索。
- **consolidate / forget**：记忆维护（巩固/遗忘）。
- **embed**：零依赖语义表示。
- **store**：持久化后端抽象。
- **adapters**：LLM 能力抽象（打分/总结）。
- **eval**：确定性评测。
- **api**：HTTP 服务。

## 依赖方向

自底向上：util → core / embed → adapters / store → write / retrieve →
consolidate / forget → fast / slow → memory → eval / api → cli。
无循环依赖，任何子包可单独 import。

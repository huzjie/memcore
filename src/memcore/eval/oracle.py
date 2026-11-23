"""确定性 oracle：写入事实 -> 查询 -> 期望命中的闭式评测。"""
from __future__ import annotations

from ..core.memory import Memory


class MemoryOracle:
    """不依赖真实大模型，验证「写入 -> 检索 -> 命中」完整链路。"""

    def __init__(self, memory: Memory | None = None):
        self.memory = memory or Memory(use_gate=False)

    def run(self, facts: list, queries: list) -> dict:
        ids = []
        for f in facts:
            item = self.memory.add(f, force=True)
            if item:
                ids.append(item.id)
        rows = []
        for q, gold in queries:
            results = self.memory.search(q, limit=5)
            pred = [r.item.id for r in results]
            gold_ids = [ids[int(i)] for i in gold]
            rows.append({"query": q, "predicted": pred, "gold": gold_ids})
        return {"items": ids, "rows": rows}

"""基准：跑 oracle，汇总 recall@k / MRR / 保留率。"""
from __future__ import annotations

from .metrics import recall_at_k, mrr, retention_rate
from .oracle import MemoryOracle
from .dataset import build_dataset


class Benchmark:
    def __init__(self, memory=None):
        self.oracle = MemoryOracle(memory)

    def run(self, k: int = 5) -> dict:
        facts, queries = build_dataset()
        out = self.oracle.run(facts, queries)
        recalls, mrrs = [], []
        for row in out["rows"]:
            recalls.append(recall_at_k(row["predicted"], row["gold"], k))
            mrrs.append(mrr(row["predicted"], row["gold"]))
        return {
            "n_items": len(out["items"]),
            "n_queries": len(queries),
            f"recall@{k}": round(sum(recalls) / len(recalls), 4),
            "mrr": round(sum(mrrs) / len(mrrs), 4),
            "retention": retention_rate(len(facts), len(out["items"])),
        }

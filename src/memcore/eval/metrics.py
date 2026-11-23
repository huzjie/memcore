"""评测指标：recall@k / MRR / 保留率。"""
from __future__ import annotations


def recall_at_k(predicted_ids: list, gold_ids: list, k: int = 5) -> float:
    """预测 top-k 里命中多少个真实相关。"""
    if not gold_ids:
        return 0.0
    hits = len(set(predicted_ids[:k]) & set(gold_ids))
    return hits / len(gold_ids)


def mrr(predicted_ids: list, gold_ids: list) -> float:
    """第一个命中的真实相关项的倒数排名。"""
    for i, pid in enumerate(predicted_ids, start=1):
        if pid in set(gold_ids):
            return 1.0 / i
    return 0.0


def retention_rate(total_written: int, total_retained: int) -> float:
    """写入门控后保留的记忆比例。"""
    if total_written <= 0:
        return 0.0
    return total_retained / total_written

"""巩固流水线：聚簇 -> 去重 -> 总结 -> 替换。"""
from __future__ import annotations

from .cluster import Clusterer
from .dedup import deduplicate
from .summarizer import Summarizer


def consolidate(items: list, llm, cluster_threshold: float = 0.70) -> list:
    """把一批记忆巩固成更少的高层记忆，返回新记忆 content 列表。

    只对 >= 2 条的簇做总结，孤立条目原样保留。
    """
    if not items:
        return []
    clusterer = Clusterer(cluster_threshold)
    summarizer = Summarizer(llm)
    out: list = []
    for cl in clusterer.cluster(items):
        cl = deduplicate(cl)
        if len(cl) >= 2:
            out.append(summarizer.summarize([it.content for it in cl]))
        else:
            out.append(cl[0].content)
    return out

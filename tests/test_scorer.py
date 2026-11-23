from memcore.retrieve.scorer import HybridScorer
from memcore.core.types import MemoryItem
from memcore.core.query import MemoryQuery


def test_scorer_range():
    s = HybridScorer()
    it = MemoryItem(content="红色", importance=0.8)
    q = MemoryQuery("红色")
    assert 0.0 <= s.score(it, q) <= 1.0

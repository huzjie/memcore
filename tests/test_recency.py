from memcore.retrieve.recency import exponential_decay, recency_score
from memcore.core.types import MemoryItem


def test_decay_monotonic():
    assert exponential_decay(0) > exponential_decay(1000000)


def test_recency_range():
    it = MemoryItem(content="x")
    assert 0.0 <= recency_score(it) <= 1.0

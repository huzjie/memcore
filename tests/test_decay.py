from memcore.forget.decay import DecayPolicy
from memcore.core.types import MemoryItem


def test_decay_newer_higher():
    p = DecayPolicy()
    old = MemoryItem(content="old")
    new = MemoryItem(content="new")
    assert p.score(new) >= p.score(old)

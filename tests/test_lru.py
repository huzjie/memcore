from memcore.forget.lru import LruPolicy
from memcore.core.types import MemoryItem


def test_lru_rank():
    p = LruPolicy()
    a = MemoryItem(content="a")
    b = MemoryItem(content="b")
    assert p.rank(a) <= p.rank(b)  # a 先创建，last_accessed 更早

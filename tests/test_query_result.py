from memcore.core.query import MemoryQuery
from memcore.core.result import MemoryResult
from memcore.core.types import MemoryItem


def test_query_roundtrip():
    q = MemoryQuery("红色", limit=3)
    d = q.to_dict()
    assert MemoryQuery.from_dict(d).query == "红色"


def test_result_roundtrip():
    it = MemoryItem(content="红色")
    r = MemoryResult(item=it, score=0.8)
    d = r.to_dict()
    r2 = MemoryResult.from_dict(d)
    assert r2.item.content == "红色"
    assert r2.score == 0.8

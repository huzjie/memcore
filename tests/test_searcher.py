from memcore.retrieve.searcher import Searcher
from memcore.core.types import MemoryItem
from memcore.core.query import MemoryQuery


def test_search_order():
    s = Searcher()
    items = [
        MemoryItem(content="用户偏好红色强调色"),
        MemoryItem(content="今天天气不错"),
    ]
    s.index(items)
    results = s.search(items, MemoryQuery("强调色", limit=1))
    assert results[0].item.content.startswith("用户偏好红色")

import os
import tempfile
from memcore.store.json_store import JsonStore
from memcore.core.types import MemoryItem


def test_persist():
    d = tempfile.mkdtemp()
    path = os.path.join(d, "m.json")
    s = JsonStore(path)
    s.add(MemoryItem(content="持久化"))
    s2 = JsonStore(path)
    assert s2.count() == 1
    assert s2.all()[0].content == "持久化"

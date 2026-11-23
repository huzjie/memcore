import os
import tempfile
from memcore import Memory


def test_json_persistence():
    d = tempfile.mkdtemp()
    url = "json://" + os.path.join(d, "m.json")
    m1 = Memory(store_url=url, use_gate=False)
    m1.add("跨进程保留", force=True)
    m2 = Memory(store_url=url, use_gate=False)
    assert m2.count() == 1

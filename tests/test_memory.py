from memcore import Memory


def test_memory_add_search(mem):
    mem.add("用户每周五提交周报", force=True)
    rs = mem.search("周报")
    assert len(rs) >= 1


def test_memory_stats(mem):
    st = mem.stats()
    assert "longterm_items" in st
    assert "working_items" in st


def test_memory_consolidate(mem):
    for i in range(6):
        mem.add(f"偏好简洁 {i}", force=True)
    n = mem.consolidate()
    assert n >= 0

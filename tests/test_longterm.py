from memcore.slow.longterm import LongTermMemory


def test_add_search():
    lt = LongTermMemory()
    lt.add("用户偏好红色", force=True)
    rs = lt.search("红色")
    assert rs and "红色" in rs[0].item.content

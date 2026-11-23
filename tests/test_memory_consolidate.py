from memcore import Memory


def test_consolidate_reduces_similar():
    mem = Memory(use_gate=False)
    for i in range(6):
        mem.add(f"用户偏好简洁排版 {i}", force=True)
    n = mem.consolidate()
    assert mem.count() < 6
    assert n > 0

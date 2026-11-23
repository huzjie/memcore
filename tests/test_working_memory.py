from memcore.fast.working_memory import WorkingMemory


def test_capacity():
    wm = WorkingMemory(capacity=3)
    for i in range(5):
        wm.add(f"m{i}")
    assert len(wm) == 3
    assert wm.peek(1)[0]["content"] == "m4"

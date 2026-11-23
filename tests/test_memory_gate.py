from memcore import Memory


def test_gate_rejects_chat():
    mem = Memory(use_gate=True)
    assert mem.add("今天天气不错，心情很好") is None


def test_gate_accepts_preference():
    mem = Memory(use_gate=True)
    assert mem.add("用户必须记住品牌强调色") is not None

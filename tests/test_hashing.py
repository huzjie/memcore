from memcore.embed.hashing import HashingVectorizer


def test_dim():
    v = HashingVectorizer(128)
    vec = v(["a", "b", "c"])
    assert len(vec) == 128


def test_nonzero():
    v = HashingVectorizer(128)
    assert sum(x != 0 for x in v(["hello"])) >= 1

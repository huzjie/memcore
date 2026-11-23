from memcore.embed.vectors import cosine, dot, l2_norm


def test_dot():
    assert dot([1, 2, 3], [4, 5, 6]) == 32


def test_cosine_same():
    assert abs(cosine([1, 0], [1, 0]) - 1.0) < 1e-9


def test_cosine_orthogonal():
    assert cosine([1, 0], [0, 1]) == 0.0


def test_l2():
    assert l2_norm([3, 4]) == 5.0

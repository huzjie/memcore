from memcore.retrieve.relevance import relevance_score


def test_relevance_self_high():
    assert relevance_score("发票", "发票") > relevance_score("发票", "天气")

from memcore.embed.tfidf import TfidfIndex


def test_tfidf_search():
    idx = TfidfIndex()
    idx.add(["生成", "发票"])
    idx.add(["天气", "不错"])
    res = idx.search(["发票"], top_k=1)
    assert res and res[0][0] == 0

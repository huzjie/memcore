from memcore.write.salience import salience_score


def test_imperative_higher():
    assert salience_score("用户必须遵守合规红线") > salience_score("今天天气不错")

from memcore.cli import main


def test_doctor():
    assert main(["doctor"]) == 0


def test_add_search():
    assert main(["add", "测试记忆", "--force"]) == 0
    assert main(["search", "测试"]) == 0


def test_eval():
    assert main(["eval"]) == 0

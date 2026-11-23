from memcore.config import build_memory, build_llm
from memcore.adapters.mock import MockLLM
from memcore.adapters.openai import OpenAICompatLLM


def test_build_llm_mock():
    assert isinstance(build_llm({}), MockLLM)


def test_build_llm_openai():
    llm = build_llm({"llm": {"provider": "openai",
                             "endpoint": "https://x.example.com"}})
    assert isinstance(llm, OpenAICompatLLM)


def test_build_memory():
    mem = build_memory({})
    assert mem.stats()["gate"] is True

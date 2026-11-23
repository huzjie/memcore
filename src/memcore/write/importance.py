"""重要性打分：默认走 LLM 适配器（mock 或真实），可复现。"""
from __future__ import annotations

from ..adapters.base import LLMAdapter

_PROMPT = (
    "请评估信息的长期留存价值，只输出 0 到 1 的数字。\n"
    "信息：{content}"
)


def importance_score(content: str, llm: LLMAdapter) -> float:
    prompt = _PROMPT.format(content=content)
    return llm.score(prompt)

"""LLM 适配器抽象：统一 complete 接口。"""
from __future__ import annotations

from abc import ABC, abstractmethod


class LLMAdapter(ABC):
    """把「生成/打分/总结」等需要智能的能力抽象成一个接口。

    打分为确定性场景提供 mock 后端；真实场景接 OpenAI 兼容网关。
    """

    @abstractmethod
    def complete(self, prompt: str, max_tokens: int = 256) -> str:
        """给定 prompt 返回文本补全。"""
        raise NotImplementedError

    def score(self, prompt: str) -> float:
        """把补全结果解析为 [0,1] 分数，默认取首行数值。"""
        text = self.complete(prompt, max_tokens=8).strip()
        try:
            val = float(text)
        except ValueError:
            val = 0.5
        return max(0.0, min(1.0, val))

    def name(self) -> str:
        return self.__class__.__name__

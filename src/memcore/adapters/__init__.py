"""LLM 适配器：确定性 mock 与 OpenAI 兼容真实后端。"""
from .base import LLMAdapter
from .mock import MockLLM
from .openai import OpenAICompatLLM

__all__ = ["LLMAdapter", "MockLLM", "OpenAICompatLLM"]

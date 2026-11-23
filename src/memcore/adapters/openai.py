"""OpenAI 兼容真实 LLM：填 endpoint/key 即可接任意网关。"""
from __future__ import annotations

import json
import urllib.request

from .base import LLMAdapter


class OpenAICompatLLM(LLMAdapter):
    """通过 HTTP 调用 OpenAI 兼容 /v1/chat/completions 端点。

    参数 endpoint 与 api_key 来自 config，缺省报错但可用 mock 兜底。
    """

    def __init__(self, endpoint: str, api_key: str = "", model: str = "gpt-4o-mini",
                 timeout: float = 30.0):
        if not endpoint:
            raise ValueError("endpoint is required for OpenAICompatLLM")
        self.endpoint = endpoint.rstrip("/")
        self.api_key = api_key
        self.model = model
        self.timeout = timeout

    def complete(self, prompt: str, max_tokens: int = 256) -> str:
        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": max_tokens,
        }
        req = urllib.request.Request(
            self.endpoint + "/v1/chat/completions",
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_key}",
            },
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=self.timeout) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        return data["choices"][0]["message"]["content"].strip()

    def name(self) -> str:
        return f"OpenAICompatLLM({self.model})"

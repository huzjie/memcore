"""配置加载：从 dict / yaml 文件构造 Memory。"""
from __future__ import annotations

from .adapters.mock import MockLLM
from .adapters.openai import OpenAICompatLLM


def build_llm(cfg: dict):
    """按配置构造 LLM 适配器。缺省 mock。"""
    provider = (cfg.get("llm") or {}).get("provider", "mock")
    if provider == "openai":
        llm_cfg = cfg["llm"]
        return OpenAICompatLLM(
            endpoint=llm_cfg.get("endpoint", ""),
            api_key=llm_cfg.get("api_key", ""),
            model=llm_cfg.get("model", "gpt-4o-mini"),
        )
    return MockLLM()


def build_memory(cfg: dict):
    from .core.memory import Memory
    store = cfg.get("store") or {}
    return Memory(
        llm=build_llm(cfg),
        store_url=store.get("url"),
        use_gate=bool(cfg.get("gate", {}).get("enabled", True)),
        max_items=int(cfg.get("forget", {}).get("max_items", 10_000)),
    )

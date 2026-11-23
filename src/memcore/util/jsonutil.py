"""JSON 序列化：支持 dataclass / 自定义对象的稳健读写。"""
from __future__ import annotations

import json
from typing import Any


def dumps(obj: Any, indent: int | None = None) -> str:
    return json.dumps(obj, ensure_ascii=False, indent=indent, default=_default)


def loads(text: str) -> Any:
    return json.loads(text)


def _default(obj: Any) -> Any:
    if hasattr(obj, "to_dict"):
        return obj.to_dict()
    if hasattr(obj, "__dataclass_fields__"):
        return {k: getattr(obj, k) for k in obj.__dataclass_fields__}
    raise TypeError(f"not JSON serializable: {type(obj).__name__}")

"""时间工具：毫秒级时间戳与 ISO 字符串互转。"""
from __future__ import annotations

import time
from datetime import datetime, timezone


def now_ms() -> int:
    return int(time.time() * 1000)


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def iso_to_ms(iso: str) -> int:
    try:
        dt = datetime.fromisoformat(iso.replace("Z", "+00:00"))
    except ValueError:
        dt = datetime.now(timezone.utc)
    return int(dt.timestamp() * 1000)


def age_ms(created_ms: int, reference_ms: int | None = None) -> int:
    ref = reference_ms if reference_ms is not None else now_ms()
    return max(0, ref - created_ms)

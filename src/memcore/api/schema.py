"""HTTP 请求 / 响应 schema 与序列化。"""
from __future__ import annotations

from ..util.jsonutil import dumps, loads


def ok(data: dict) -> dict:
    return {"ok": True, "data": data}


def err(message: str, code: int = 400) -> dict:
    return {"ok": False, "error": {"message": message, "code": code}}


def to_json(obj) -> str:
    return dumps(obj)


def from_json(text: str):
    return loads(text)

"""OpenAI 兼容 HTTP 服务：/v1/memories + /health。"""
from .server import serve

__all__ = ["serve"]

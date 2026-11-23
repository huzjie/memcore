"""轻量日志：标准库 logging 封装，避免第三方依赖。"""
from __future__ import annotations

import logging
import sys

_FORMAT = "%(asctime)s %(levelname)-7s %(name)s: %(message)s"
_DEFAULT_LEVEL = logging.INFO

_configured = False


def configure_logging(level: int | str = _DEFAULT_LEVEL) -> None:
    global _configured
    logging.basicConfig(level=level, format=_FORMAT, stream=sys.stderr)
    _configured = True


def get_logger(name: str = "memcore") -> logging.Logger:
    if not _configured:
        configure_logging()
    return logging.getLogger(name)

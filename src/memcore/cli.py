"""命令行入口：doctor / add / search / serve / eval / consolidate / forget。"""
from __future__ import annotations

import argparse
import sys

from .config import build_memory
from .core.memory import Memory
from .eval.benchmark import Benchmark
from .util.jsonutil import dumps, loads


def _load_config(path: str | None) -> dict:
    if not path:
        return {}
    try:
        import yaml  # 可选依赖
    except ImportError:
        yaml = None
    if yaml is None:
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def cmd_doctor(args) -> int:
    mem = build_memory(_load_config(args.config))
    print("✅ memcore 就绪")
    for k, v in mem.stats().items():
        print(f"  {k}: {v}")
    return 0


def cmd_add(args) -> int:
    mem = build_memory(_load_config(args.config))
    item = mem.add(args.content, force=args.force)
    if item:
        print(f"✅ 已写入记忆 {item.id[:8]} (importance={item.importance:.3f})")
        return 0
    print("⏭️ 写入门控拒绝（重要性不足，未写入长期记忆）")
    return 0


def cmd_search(args) -> int:
    mem = build_memory(_load_config(args.config))
    results = mem.search(args.query, limit=args.limit)
    if not results:
        print("（无结果）")
        return 0
    for i, r in enumerate(results, 1):
        print(f"{i}. [{r.score:.3f}] {r.item.content}")
    return 0


def cmd_serve(args) -> int:
    mem = build_memory(_load_config(args.config))
    from .api.server import serve
    serve(mem, host=args.host, port=args.port)
    return 0


def cmd_eval(args) -> int:
    mem = build_memory(_load_config(args.config))
    result = Benchmark(mem).run(k=args.k)
    print(dumps(result, indent=2))
    return 0


def cmd_consolidate(args) -> int:
    mem = build_memory(_load_config(args.config))
    n = mem.consolidate()
    print(f"✅ 巩固完成，合并掉 {n} 条记忆")
    return 0


def cmd_forget(args) -> int:
    mem = build_memory(_load_config(args.config))
    n = mem.forget()
    print(f"✅ 遗忘淘汰 {n} 条记忆")
    return 0


def main(argv: list | None = None) -> int:
    ap = argparse.ArgumentParser(prog="memcore", description="记忆原生 Agent 记忆内核")
    ap.add_argument("--config", help="配置文件路径（可选 yaml）")
    sub = ap.add_subparsers(dest="cmd")

    sub.add_parser("doctor", help="环境自检")
    p_add = sub.add_parser("add", help="写入一条记忆")
    p_add.add_argument("content")
    p_add.add_argument("--force", action="store_true")
    p_search = sub.add_parser("search", help="检索记忆")
    p_search.add_argument("query")
    p_search.add_argument("--limit", type=int, default=5)
    p_serve = sub.add_parser("serve", help="启动 HTTP 服务")
    p_serve.add_argument("--host", default="127.0.0.1")
    p_serve.add_argument("--port", type=int, default=8080)
    p_eval = sub.add_parser("eval", help="运行内置基准")
    p_eval.add_argument("--k", type=int, default=5)
    sub.add_parser("consolidate", help="巩固长期记忆")
    sub.add_parser("forget", help="执行遗忘淘汰")

    args = ap.parse_args(argv)
    if args.cmd is None:
        ap.print_help()
        return 0
    handlers = {
        "doctor": cmd_doctor, "add": cmd_add, "search": cmd_search,
        "serve": cmd_serve, "eval": cmd_eval,
        "consolidate": cmd_consolidate, "forget": cmd_forget,
    }
    return handlers[args.cmd](args)


if __name__ == "__main__":
    sys.exit(main())

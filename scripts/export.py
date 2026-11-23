"""导出记忆为 JSONL。"""
import sys
from memcore import Memory

mem = Memory(store_url=sys.argv[1] if len(sys.argv) > 1 else None,
             use_gate=False)
for it in mem.all():
    print(it.to_dict())

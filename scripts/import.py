"""从 JSONL 导入记忆。"""
import json
import sys
from memcore import Memory

mem = Memory(use_gate=False)
path = sys.argv[1] if len(sys.argv) > 1 else "import.jsonl"
with open(path, encoding="utf-8") as f:
    for line in f:
        d = json.loads(line)
        mem.add(d.get("content", ""), force=True)
print("imported", mem.count())

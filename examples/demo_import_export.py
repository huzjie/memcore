"""导入导出示例：JSONL 格式。"""
import json
from memcore import Memory

mem = Memory(use_gate=False)
mem.add("导出测试", force=True)

# 导出
lines = [json.dumps(it.to_dict(), ensure_ascii=False) for it in mem.all()]
open("export.jsonl", "w", encoding="utf-8").write("\n".join(lines))
print("已导出", len(lines), "条到 export.jsonl")

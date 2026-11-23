# 快速开始

```bash
pip install -r requirements.txt
python -m memcore doctor
python -m memcore add "用户每周五提交周报，收件人 shuangjinwei" --force
python -m memcore search "周报"
python -m memcore eval
```

## 编程方式

```python
from memcore import Memory

mem = Memory(store_url="sqlite://memory.db")
mem.add("用户偏好红色 #E60012 作为强调色", force=True)
results = mem.search("强调色")
for r in results:
    print(r.score, r.item.content)
```

## 接真实 LLM

```yaml
llm:
  provider: openai
  endpoint: https://your-gateway.example.com
  api_key: sk-xxx
  model: gpt-4o-mini
store:
  url: sqlite://memory.db
```

"""接真实 LLM 示例：写入门控与巩固切换真实模型。"""
from memcore import Memory
from memcore.adapters.openai import OpenAICompatLLM

llm = OpenAICompatLLM(endpoint="https://your-gateway.example.com",
                      api_key="sk-xxx", model="gpt-4o-mini")
mem = Memory(llm=llm, use_gate=True)
it = mem.add("用户必须遵守合规红线", force=False)
print("写入结果:", it)

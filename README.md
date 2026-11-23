# memcore —— 记忆原生 Agent 的记忆内核

> **把「记忆原生大模型」的「快慢记忆」原理，工程化成一个填配置就能跑的记忆内核。**
> 纯 Python、零第三方依赖，给任意 Agent / LLM 应用挂载「长期记忆」。

[![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/)
[![License MIT](https://img.shields.io/badge/license-MIT-green)](./LICENSE)

---

## 👀 它解决什么问题？

现在大多数 Agent「记性不好」：把历史对话重新塞进上下文窗口，窗口一大就过载，
聊得越长越容易忘掉你最早交代的偏好。**memcore 把记忆从「临时上下文」里独立出来**，
拆成两个通道：

| 通道 | 类比 | 承载什么 | 生命周期 |
|---|---|---|---|
| **快记忆**（working） | 工作记忆 | 当前会话最近 N 条 | 会话内 |
| **慢记忆**（longterm） | 长期记忆 | 跨会话的高价值事实 / 偏好 | 持久化 |

慢记忆**不是每条都存**——它有一个**写入门控**，只把「够重要、够新颖」的内容写进去；
用的时候按「相关性 + 时间 + 重要性」混合检索召回；记忆库太大还会**自动巩固、自动遗忘**。

---

## ⚡ 30 秒上手

```bash
git clone https://github.com/huzjie/memcore.git
cd memcore
pip install -r requirements.txt   # 仅 PyYAML，可选
python -m memcore doctor          # 自检
python -m memcore add "用户偏好红色 #E60012 作为强调色" --force
python -m memcore search "强调色"
python -m memcore eval            # 内置基准
python -m memcore serve           # 启动 HTTP 服务
```

**填配置接真实 LLM**：把 `config.example.yaml` 复制为 `config.yaml`，
`llm.provider` 改为 `openai` 并填 `endpoint` / `api_key`，写入门控与巩固的「打分 / 总结」
即切换为真实模型，其余逻辑不变。

---

## 🧭 技术原理：快慢记忆是怎么落地的？

对应「记忆原生大模型」的三个核心机制，memcore 分别工程化成：

1. **快慢记忆双通道** → `fast.WorkingMemory`（环形缓冲）+ `slow.LongTermMemory`（持久化 store）。
2. **原生记忆模块（模型自己写/更新记忆）** → `write.WriteGate` 写入门控：
   `score = 0.40×importance + 0.35×salience + 0.25×novelty`，超阈值才落长期记忆，
   而不是把每条对话无脑塞进去。
3. **记忆检索 / 遗忘** → `retrieve.Searcher`（relevance + recency + importance 加权）
   与 `forget.Evictor`（预算淘汰 + 指数衰减）。

**零依赖怎么实现语义相关？** `embed` 包内置了中文分词（停用词 + 二元组）、TF-IDF、
BM25、特征哈希，`retrieve.relevance` 用 BM25+TF-IDF 混合稀疏召回，无需向量数据库。

---

## 📁 项目结构

```
src/memcore/
├── core/          # MemoryItem / MemoryQuery / MemoryResult / Memory 门面
├── fast/          # 快记忆（工作记忆环形缓冲）
├── slow/          # 慢记忆（长期记忆银行）
├── write/         # 写入门控（显著性/新颖性/重要性/冲突）
├── retrieve/      # 混合检索（时间衰减+相关性+重要性）
├── consolidate/   # 记忆巩固（聚簇/去重/总结）
├── forget/        # 遗忘（LRU/衰减/预算淘汰）
├── embed/         # 零依赖嵌入（分词/TF-IDF/BM25/哈希）
├── store/         # 存储后端（内存/JSON/SQLite）
├── adapters/      # LLM 适配（确定性 mock / OpenAI 兼容）
├── eval/          # 评测（recall@k / MRR / 保留率）
└── api/           # OpenAI 兼容 HTTP 服务
```

完整架构见 [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)，调参见 [docs/TUNING.md](docs/TUNING.md)。

---

## 🚀 复用要点（干货）

- **中文分词先加停用词表**：否则「生成一张发票」和「生成一张流程图」会因「一张」撞车。
- **新颖性用一个相似度阈值判重**：`novelty = 1 - max_cosine`，超过阈值直接判重复，
  避免同一条偏好被反复写入。
- **写入门控才是「记忆」和「日志」的分界线**：没有门控，长期记忆就退化成聊天记录。
- **评测用闭式 oracle**：写入 N 条事实 → 问 M 个问题 → 断言命中，无需大模型打分，CI 可复现。

详见 [INTRO.md](INTRO.md)（本期完整技术拆解）。

---

## 📜 License

[MIT](./LICENSE)

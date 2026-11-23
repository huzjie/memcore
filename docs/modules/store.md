# 存储后端
`Store` 抽象，`MemoryStore` / `JsonStore` / `SqliteStore` 三种实现，
`factory.create_store(url)` 按 URL 创建。
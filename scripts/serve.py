"""启动服务。"""
from memcore.core.memory import Memory
from memcore.api.server import serve

serve(Memory(use_gate=False), host="0.0.0.0", port=8080)

from memcore.store.factory import create_store
from memcore.store.memory_store import MemoryStore
from memcore.store.json_store import JsonStore
from memcore.store.sqlite_store import SqliteStore


def test_factory_memory():
    assert isinstance(create_store("memory://"), MemoryStore)


def test_factory_json():
    assert isinstance(create_store("json://x.json"), JsonStore)


def test_factory_sqlite():
    assert isinstance(create_store("sqlite://x.db"), SqliteStore)

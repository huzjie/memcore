import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import pytest
from memcore import Memory


@pytest.fixture
def mem():
    return Memory(use_gate=False)

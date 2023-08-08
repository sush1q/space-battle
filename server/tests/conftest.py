import sys
sys.path.append('.')

import pytest
from server import *


@pytest.fixture(autouse=True)
def clear_event_loop():
    EventLoop.clear()


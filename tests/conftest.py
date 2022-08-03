# these fixtures can be shared between test modules. Note that the filename should be "conftest.py"
import pytest
from src.accumulator.accumulator import Accumulator


@pytest.fixture
def shareable_fixture():
    return Accumulator()
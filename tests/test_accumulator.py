import pytest

from src.accumulator.accumulator import Accumulator


@pytest.fixture
def accumulator_fixture(): # default scope to function
    return Accumulator()

# @pytest.fixture
# def accum_fixture_2(scope="session"): # other values could be class, module or package
#     # we can have some setup here
#     yield Accumulator() # at this point, python goes to the test using the fixture
#     # whatever is after yield gets run after we are done with the test


def test_accumulator_init(accumulator_fixture):
    assert accumulator_fixture.count == 0


def test_add_default(accumulator_fixture):
    accumulator_fixture.add()
    assert accumulator_fixture.count == 1


def test_add_more(accumulator_fixture):
    accumulator_fixture.add(5)
    assert accumulator_fixture.count == 5


def test_errors_on_setting_count(shareable_fixture):
    with pytest.raises(AttributeError) as e:
        shareable_fixture.count = 4

    assert "can't set attribute" in str(e.value)

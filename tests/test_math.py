import pytest


def test_one_plus_one():
    assert 1 + 1 == 2


def test_one_plus_two():
    a = 1
    b = 2
    c = 3
    assert a + b == c


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0

    assert 'division by zero' in str(e.value)


multiplication_test_samples = [
    (5, 10, 50),    # positive factors
    (-5, -10, 50),  # negative factors
    (10, 1, 10),    # multiply by 1
    (10, 0, 0)      # multiply by 0
]


@pytest.mark.parametrize('a, b, expected_result', multiplication_test_samples)
def test_multiplication(a, b, expected_result):
    assert a * b == expected_result

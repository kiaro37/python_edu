import pytest
from helpers import calc_discount

# def test_discount_5_percent():
#     assert calc_discount(100, 5) == 95
#
# def test_discount_10_percent():
#     assert calc_discount(200, 10) == 180

@pytest.mark.parametrize(
    "price, percent, expected",
    [
        (100, 5, 95),
        (200, 10, 180),
        (50, 0, 50)
    ]
)
def test_calc_discount(price, percent, expected):
    assert calc_discount(price, percent) == expected
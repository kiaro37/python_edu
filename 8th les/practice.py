# Мини-практика
# В helpers.py уже есть функция calc_discount(price, percent)
#
# В test_utils.py добавь параметризованный тест для неё
#
# Проверь, что все кейсы проходят:
#
# (100, 5, 95)
# (200, 10, 180)
# (50, 0, 50)

import pytest
from helpers import calc_discount

@pytest.mark.parametrize(
    "price, percent, expected",
    [
        (100, 5, 95),
        (200, 10, 180),
        (50, 0, 50)
     ]
)

def test_calc_discount(price,percent, expected):
    calc_discount(price,percent) == expected
# Мини-практика:
# Создай фикстуру sample_user в test_utils.py (или в conftest.py, если хочешь использовать глобально)
#
# Фикстура должна возвращать словарь:
#
# {"name": "Masha", "age": 25, "is_active": True}
#
# Напиши тест test_user_name_not_empty(sample_user) — проверь, что name не пустой


from test_utils import sample_user
import pytest

def test_user_name_not_empty(sample_user):
    assert sample_user["name"].strip()         #strip удаляет все пустые жлементы типа пробелов,
                                                # а assert проверяет, что значение не пустое
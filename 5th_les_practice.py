# Мини-практика
# Напиши:
#
# Функцию hello_user(name), которая печатает приветствие для пользователя.
#
# Функцию is_adult(age), которая возвращает True, если возраст ≥ 18.
#
# Функцию calc_discount(price, percent), которая возвращает цену с учётом скидки.

def hello_user(name):
    print(f"Привет {name}!")

hello_user("Маша")

def is_adult(age):
    if age<0:
        raise ValueError("Возраст не может быть отрицательным")
    return age>=18

print(is_adult(17))

def calc_discount(price, percent):
    if price<0 or percent<0:
        raise ValueError("Цена или процент скидки не могут быть отрицательными")
    else:
        return price-price*percent/100

print(calc_discount(100, 5))

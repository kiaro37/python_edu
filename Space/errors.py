# # Синтаксис try/exept
#
# try:
#     x = 1 / 0
# except ZeroDivisionError:
#     print("На ноль делить нельзя!")
#
# # Множественные исключения
#
# try:
#     with open("data.txt") as f:
#         data = f.read()
#     result = 100 / int(data)
# except FileNotFoundError:
#     print("Файл не найден")
# except ValueError:
#     print("В файле не число")
# except ZeroDivisionError:
#     print("На ноль делить нельзя")
#
# # else и finally
#
# try:
#     print("Всё ок")
# except:
#     print("Ошибка")
# else:
#     print("Ошибок не было")
# finally:
#     print("Это выполнится в любом случае")
#
# # Упражнение
#
from pickletools import read_uint1


def load_number(path):
    try:
        with open(path, "r") as f:
            return int(f.read())
    except FileNotFoundError:
        return ("Файл не найден")
    except ValueError:
        return ("Это не число")

print(load_number("number.txt"))

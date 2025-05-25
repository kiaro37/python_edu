# Создадим простой класс

class User:
    def __init__(self, username):
        self.__username = username           # username стало приватной переменной

    def get_username(self):
        return self.__username

    def set_username(self, new_name):
        if new_name:
            self.__username = new_name
        else:
            print("Поле не может быть пустым")


user = User("Masha")
print(user.get_username())

user.set_username("Dasha")
print(user.get_username())

user.set_username("")

# Сделай похожее:
# Класс Admin с приватным __access_level
# Метод get_access() и set_access(), где set разрешает только значения "read", "write", "admin"

class Admin:
    def __init__(self, access_level):
        self.__access_level = None
        self.set_access_level(access_level)

    def get_access_level(self):
        return self.__access_level

    def set_access_level(self, new_level):
        allowed_levels = ["read", "write", "admin"]
        if new_level in allowed_levels:
            self.__access_level = new_level
        else:
            print("Введенный статус запрещен")

level = Admin("read")
print(level.get_access_level())

level.set_access_level("admin")
print(level.get_access_level())

level.set_access_level("user")
print(level.get_access_level())


class Car:
    def __init__(self, year):
        self.year = year

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, new_year):
        if new_year > 1990:
            self.__year = new_year
        else:
            raise ValueError(f"Авто не может быть такого года выпуска")

    def get_info(self):
        return f"Авто {self.__year} года выпуска!"

car = Car(1991)
print(car.get_info())
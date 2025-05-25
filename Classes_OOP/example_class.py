# ✅ Объяснение по шагам:
# Конструкция	Что делает
# class User:	Создаёт новый класс User
# __init__	Метод-конструктор, вызывается при создании
# self	Ссылка на текущий объект
# self.name = name	Сохраняет имя внутри объекта
# u = User(...)	Создаёт объект класса
# u.greet()	Вызывает метод для объекта

class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def show_info(self):
        return (f"{self.brand} - {self.year} года выпуска")

my_car = Car("Toyota", 2000)
print(my_car.show_info())

# 🛠 Упражнение
# Попробуй сам:
# 1. Создай базовый класс User, у которого есть username.
# 2. От него унаследуй класс Admin, добавь туда access_level.
# 3. Сделай метод show_access(), который выводит имя и уровень доступа.

class User():
    def __init__(self, username):
        self.username = username

    def start(self):
        print(f"My name is {self.username}")

class Admin(User):
    def __init__(self, username, access_level):
        super().__init__(username)
        self.access_level = access_level

    def show_access(self):
        print(f"{self.username} имеет уровень доступа {self.access_level}")

my_user = Admin("Masha", "red")
my_user.show_access()

class User:                                         # класс родитель
    def __init__(self, username):
        self.username = username

    def say_hello(self):
        print(f"Hello, I'm user {self.username}!")

# class Admin(User):                                        # класс наследник (потомок)
#     def show_panel(self):
#         print(f"Admin panel for {self.username}")

# class Admin(User):                                         # переопределение метода родительского класса
#     def say_hello(self):
#         print(f"Now I'm admin, my name is {self.username}.")

class Admin(User):                                            # добавление к методу родительского класса
    def say_hello(self):
        super().say_hello()
        print("I have special privileges!")

admin = Admin("Anna")
admin.say_hello()


#Практика для тебя:
# 1. Создай базовый класс Page:
# метод open() — печатает Открытие страницы
# 2. Создай потомок LoginPage:
# переопредели open() — дополни: Открытие страницы -> Ввод логина

class Page:
    def open(self):
        print("Открытие страницы")

class LoginPage(Page):
    def open(self):
        super().open()
        print("Ввод логина")

class ProfilePage(Page):
    def open(self):
        super().open()
        print("Загрузка профиля пользователя")

page = LoginPage()
page.open()

print("-----")

profile = ProfilePage()
profile.open()
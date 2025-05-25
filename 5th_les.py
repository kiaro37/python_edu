# Функции

#Объявление функции

# def имя_функции(параметры):
#     # тело функции
#     return результат

def greet():                             #объявление функции
    print("Привет тестировщик")

greet()                                  #вызов функции

def greet(name):
    print(f"Привет, {name}!")

greet("Маша")



def square(x):
    return x * x

x = 4
result = square(x)
print(f"Квадратный корень {x} -- > {result}")  # → 16


def greet(name="гость"):
    print(f"Привет, {name}!")

greet()           # → Привет, гость!
greet("Иван")     # → Привет, Иван!

def add(a, b):
    return a + b

print(add(3, 5))  # → 8

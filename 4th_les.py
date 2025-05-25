#Операции со строками:

text = "Hello, world!"     # строка (str)

print(len(text))         # длина строки
print(text.lower())      # в нижний регистр
print(text.upper())      # в верхний регистр
print(text.replace("world", "Python"))  # замена подстроки
print("Hello" in text)   # проверка наличия подстроки
print(text[0])           # первый символ
print(text[-1])          # последний символ

#Операции со списками

fruits = ["apple", "banana", "plum"]      # список (list)

print(fruits[0])        # доступ по индексу
print(fruits[-1])       # последний элемент

fruits.append("orange") # добавить элемент
fruits.remove("banana") # удалить по значению
print(len(fruits))      # длина списка

for fruit in fruits:    # перебор
    print(fruit)

numbers = list(range(1, 6))  # [1, 2, 3, 4, 5]     # Быстрое создание списков
print(numbers)

#Операции со словарями

user ={
    "name": "Alice",
    "age": 30,
    "is_admin": True
}

print(user["name"])          # доступ по ключу
user["age"] = 31             # изменение значения
user["email"] = "a@b.com"    # добавление новой пары
del user["is_admin"]         # удаление

for key in user:
    print(f"{key} -> {user[key]}")

if "email" in user:
    print("Email найден")

# Попробуй сам:
#
# Создай строку message = "Automation Testing" и выведи её в нижнем регистре.
#
# Создай список из 3 любимых фруктов и выведи их через цикл.
#
# Создай словарь user с полями username, role, is_active — и выведи все ключи и значения.

message = "Automation Testing"
print(message.lower())

like_fruits = ["apple", "orange", "kiwi"]
for fruit in like_fruits:
    print(fruit)

user = {
    "username": "Masha",
    "role": "wife",
    "is_active": True
}

for key in user:
    print(f"{key} --> {user[key]}")
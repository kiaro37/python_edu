import json
#
# # 🔹 Чтение файла (полное):
#
# with open("example.txt", "r", encoding="utf-8") as file:
#     content = file.read()
#     print(content)
#
# # 🔹 Построчное чтение:
#
# with open("example.txt", "r", encoding="utf-8") as file:
#     for line in file:
#         print(line.strip())
#
# # 🔹 Запись в файл (перезапись):
#
# with open("output.txt", "w", encoding="utf-8") as file:
#     file.write("Hello, QA engineer!\n")
#
# #🔹 Добавление в файл:
#
# with open("output.txt", "a", encoding="utf-8") as file:
#     file.write("Добавили ещё строку\n")
#
# # 🔹 Чтение .json
#
# # import json
#
# with open("data.json", "r", encoding="utf-8") as file:
#     data = json.load(file)
#
# print(data["username"])  # → admin
#
# #🔹 Запись .json
#
# user = {"name": "QA_user", "is_active": True}
#
# with open("new_user.json", "w", encoding="utf-8") as file:
#     json.dump(user, file, indent=2)


user = {"name": "Masha", "role": "QA", "is_active": True }

with open("user.json", "w", encoding="utf-8") as file:
    json.dump(user, file)

with open("user.json", "r", encoding="utf-8") as f:
    user = json.load(f)

print(f"Пользователь: {user["name"]} ({user["role"]})")

user["is_active"] = False

with open("user.json", "w", encoding="utf-8") as f:
    json.dump(user, f, indent=2)

print(f"Пользователь: {user["name"]} ({user["is_active"]})")
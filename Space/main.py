# Методы строк

print(("  hello  ").strip())
print("token_abc".startswith("tok"))
print("fake_token".replace("_", " "))
print(",".join(["apple", "orange"]))
print("apple, plum".split(","))
print("abc" in "abcfg")

text = "  Hello, my name is QA_user.  "
print(text.strip())                        # Убрать пробелы по краям
print(text.lower())                        # Привести к нижнему регистру
print("QA" in text)                        # Проверка подстроки
print(text.replace("QA_user", "Tester"))   # Замена
print(text.split(","))                     # Разделить по запятой


# Методы списков

fruits = ["apple", "banana"]
fruits.append("kiwi")
fruits.insert(1, "orange")
fruits.remove("banana")
print(fruits)
print(sorted(fruits))

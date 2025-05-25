
for i in [1,2,3]:          #выводим числа из списка
    print(f"Число {i}")

for i in range(1,6):       #выводим числа из диапозона от 1 до 5, range выводит от 0 до n-1
    print(i)

i=0                        #выводим i до тех пор пока i меньше 5
while i<5:
    print(i)
    i+=1

for i in range(10):        #выводим i до тех пор пока i не будет равно 5 (оператор break)
    if i==5:
        break
    print(i)

for i in range(5):           #выводим i и пропускаем из списка 2 (оператор continue)
    if i==2:
        continue
    print(i)

for letter in "Hello":         #выводим элементы строки (в данном случае буквы)
    print(letter)

fruits = ['apple', 'plum', 'banana'] #выводим элементы списка
for fruit in fruits:
    print(fruit)

user = {"name": "Alice", "age": 28}   #выводи элементы словаря (словарь содержит ключи и значения)
for key in user:
    print(f"{key} = {user[key]}")
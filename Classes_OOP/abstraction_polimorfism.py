from abc import ABC, abstractmethod

class Animal():
    def voice(self):
        pass

class Cat(Animal):
    @abstractmethod
    def voice(self):
        print(f"Мяу")

class Dog(Animal):
    def voice(self):
        print(f"Гав")

cat = Cat()
cat.voice()

dog = Dog()
dog.voice()
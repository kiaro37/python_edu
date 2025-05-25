from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def voice(self):
        pass
    @abstractmethod
    def move(self):
        pass

class Bird(Animal):
    def voice(self):
        print("Чирик")

    def move(self):
        print("Летает")

class Fish(Animal):
    def voice(self):
        print("(Молчание)")

    def move(self):
        print("Плывет")

class Tiger(Animal):
    def voice(self):
        print("Ррррр!")

    def move(self):
        print("Бежит")


bird = Bird()
fish = Fish()
tiger = Tiger()

animals = [bird, fish, tiger]

for animal in animals:
    animal.voice()
    animal.move()
    print("---")
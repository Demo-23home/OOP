

class Animal:
    alive = True
    

class Dog(Animal):
    def speak(self) -> None:
        print("WOOF!")

class Cat(Animal):
    def speak(self) -> None:
        print("MEWO!")


class Car:
    alive = False
    
    def speak(self) -> None:
        print("HONK!")

animals = [Dog(), Cat(), Car()]


# if it walks like a duck, and quacks like a duck, then it must be a duck.

for animal in animals:
    animal.speak()
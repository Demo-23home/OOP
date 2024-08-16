class Animal:
    def __init__(self, name) -> None:
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating ")

    def sleep(self):
        print(f"{self.name} is sleeping ")


class Dog(Animal):
    pass


class Cat(Animal):
    pass


class Mouse(Animal):
    pass


dog = Dog("Scoope")
cat = Cat("Garfield")
mouse = Mouse("Mickey")

print(cat.name)
print(cat.is_alive)
cat.eat()

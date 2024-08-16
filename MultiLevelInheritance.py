class Animal:
    
    def __init__(self, name):
        self.name = name
    
    
    def eat(self) -> None:
        print(f"{self.name} is eating")
        
        
    def sleep(self) -> None: 
        print(f"{self.name} is sleeping")
        


class Preditor(Animal):
    def hunt(self) -> None:
        print(f"{self.name} Is Hunting ")
        
        
class Prey(Animal):
    def flee(self) -> None:
        print("RUN!!")
        
        



class Fish(Preditor, Prey):
    def swim(self) -> None:
        print("fish is swimming ")


class Rabbit(Prey):
    pass


class Hawk(Preditor):
    pass





fish:Fish = Fish("Memo")
fish.eat()
fish.swim()
fish.flee()
fish.hunt()
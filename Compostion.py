class Engine:
    def __init__(self, horse_power: int) -> None:
        self.horse_power = horse_power


class Wheel:
    def __init__(self, size: float) -> None:
        self.size = size


class Car:
    def __init__(
        self, model: int, make: str, horse_power: int, wheel_size: float
    ) -> None:
        self.model = model
        self.make = make
        self.engine = Engine(horse_power)
        self.wheels = [Wheel(wheel_size) for _ in range(4)]

    def display_car(self) -> str:
        return f"{self.make}, {self.model}, {self.engine.horse_power}hp, {self.wheels[0].size}in"


car = Car(2024, "Ford", 250, 22.4)

print(car.display_car())

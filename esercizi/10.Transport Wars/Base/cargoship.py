from typing import override
from spaceship import Spaceship

class CargoShip(Spaceship):
    def __init__(self, name: str, max_load: int):
        super().__init__(name)
        if max_load < 0:
            print("Max load can't be less than 0")
        self.__max_load = max_load
        self.__current_load = 0

    @property
    def max_load(self):
        return self.__max_load

    @property
    def current_load(self):
        return self.__current_load

    def load(self, amount: float):
        if (self.__current_load + amount) > self.__max_load:
            print(f"Error: Cannot load {amount}.")
        else:
            self.__current_load += amount

    @override
    def fly(self, distance: float):
        original_fuel = self.fuel
        super().fly(distance)
        if self.fuel < original_fuel:
            extra_consumption = distance // 10
            if self.fuel >= extra_consumption:
                self.fuel -= extra_consumption
                print(f"Consumo extra applicato per carico pesante: -{extra_consumption} unità.")
            else:
                print("Attenzione: Carburante esaurito a causa del peso del carico!")
                self.fuel = 0

cargo = CargoShip("etetyyty", 100)

cargo.fly(1000000)
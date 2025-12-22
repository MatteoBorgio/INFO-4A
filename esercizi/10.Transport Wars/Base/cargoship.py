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

    def fly(self, distance: float):
        super().fly(distance)
        consumption = distance // 10
        if consumption > self.__fuel:
            print("Carburante insufficiente. Viaggio annullato.")
        else:
            self.__fuel -= consumption
            print("Viaggio completato")


cargo = CargoShip("etetyyty", 100)

cargo.fly(1000000)
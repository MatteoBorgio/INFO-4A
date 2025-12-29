from typing import final, override, final

class Spaceship:
    def __init__(self, name: str):
        if name == "":
            raise ValueError("Name can't be an empty string")
        self.__name = name
        self.__fuel = 100

    @property
    def name(self):
        return self.__name

    @property
    def fuel(self):
        return self.__fuel
    
    @fuel.setter 
    def fuel(self, value):
        self.__fuel = value

    def fly(self, distance: float):
        consumption = distance // 10
        if consumption > self.__fuel:
            print("Carburante insufficiente. Viaggio annullato.")
        else:
            print(f"{self.__name} percorre {distance} anni luce.")
            self.__fuel -= consumption

    @final
    def dock(self):
        print(f"{self.__name} esegue la procedura di attracco standard.")

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

@final
class ExplorationProbe(Spaceship):
    def __init__(self, name: str):
        super().__init__(name)

    @override
    def fly(self, distance: float):
        if distance < 100:
            print("Viaggio gratutio. Nessun carburante utilizzato.")
        else:
            super().fly(distance)

    def scan(self):
        print(f"{self.name} scansiona l'area.")

class SupplyDrone(Spaceship):
    def __init__(self, name: str, value: int, hack_time: int):
        super().__init__(name)
        if value < 0:
            raise ValueError("Value can't be less than 0")
        if hack_time < 0:
            raise ValueError("Hack time can't be less than 0")
        self.__value = value
        self.__hack_time = hack_time
    
    @property
    def value(self):
        return self.__value
    
    @property
    def hack_time(self):
        return self.__hack_time
    
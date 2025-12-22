from typing import final

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
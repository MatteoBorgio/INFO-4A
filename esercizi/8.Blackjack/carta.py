class Carta:
    def __init__(self, seme: str, rango: str):
        if seme not in ["Cuori", "Picche", "Fiori", "Quadri"]:
            raise ValueError("Seme non valido")
        if rango not in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]:
            raise ValueError("Rango non valido")
        self.__seme = seme
        self.__rango = rango

    @property
    def seme(self) -> str:
        return self.__seme
    
    @property
    def rango(self) -> str:
        return self.__rango
    
    @property
    def valore(self) -> int:
        if self.__rango in ["J", "Q", "K"]:
            return 10
        if self.__rango == "A":
            return 11
        return int(self.__rango)

    def __str__(self):
        return f"{self.rango} di {self.seme}"

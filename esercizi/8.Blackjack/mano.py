class Mano:
    def __init__(self):
        self.__carte = []

    @property
    def carte(self) -> list:
        return self.__carte

    def aggiungi_carta(self, carta) -> None:
        self.__carte.append(carta)

    def get_carte(self) -> list:
        return self.__carte
    
    def svuota(self) -> None:
        self.__carte = []

    def lunghezza(self) -> int:
        return len(self.__carte)
    
    def __str__(self):
        stringhe_carte = ", ".join([str(carta) for carta in self.__carte])
        return f"[{stringhe_carte}]"
    

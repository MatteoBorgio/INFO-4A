from random import shuffle

class Mazzo:
    def __init__(self, lista_carte: list):
        self.__carte = lista_carte

    def mescola(self) -> None:
        shuffle(self.__carte)
    
    def pesca(self):
        if self.__carte == []:
            raise IndexError("Il mazzo non può essere vuoto")
        return self.__carte.pop()
    
    def lunghezza(self) -> int:
        return len(self.__carte)
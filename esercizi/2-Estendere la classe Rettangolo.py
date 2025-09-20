from random import randint

class Rettangolo: 
    def __init__(self, base: int, altezza: int):
        self.base = base
        self.altezza = altezza
        self.area = self.base * self.altezza
        
    def perimetro(self) -> int:
        return 2 * (self.base + self.altezza)
        
    def is_quadrato(self) -> bool:
        return self.base == self.altezza
        
    def ridimensiona(self, fattore: int) -> None:
        self.base *= fattore
        self.altezza *= fattore
        self.area = self.base * self.altezza
        
    def visualizza(self) -> None:
        print(f"--- Rettangolo ---\n"
              f"Base: {self.base}\n"
              f"Altezza: {self.altezza}\n"
              f"Area: {self.area}")

class Cerchio:
    def __init__(self, raggio: int):
        self.raggio = raggio
        self.area = 3.14 * (raggio ** 2)
        self.circonferenza = 3.14 * (2 * raggio)
        
    def visualizza(self) -> None:
        print(f"\n--- Cerchio ---\n"
              f"Raggio: {self.raggio}\n"
              f"Area: {self.area}\n"
              f"Circonferenza: {self.circonferenza}")

def get_lato() -> int:
    return randint(1, 50)

def figura_con_area_maggiore(figura1: str, figura2: str, area_figura1: float, area_figura2: float) -> None:
    if area_figura1 > area_figura2:
        print(f"\nLa figura con l'area maggiore è il {figura1}.")
    elif area_figura2 > area_figura1:
        print(f"\nLa figura con l'area maggiore è il {figura2}.")
    else:
        print("\nLe due figure hanno la stessa area.")

def main() -> None:
    rettangolo_casuale = Rettangolo(get_lato(), get_lato())
    cerchio_casuale = Cerchio(get_lato())
    rettangolo_casuale.visualizza()
    cerchio_casuale.visualizza()
    figura_con_area_maggiore("rettangolo", "cerchio", rettangolo_casuale.area, cerchio_casuale.area)

if __name__ == "__main__":
    main()
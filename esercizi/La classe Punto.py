import math

class Punto:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def distanza_origine(self) -> float:
        distanza = math.sqrt((math.pow(self.x, 2)) + (math.pow(self.y, 2)))
        return distanza
    
    def distanza(self, altro_punto: "Punto") -> float:
        distanza_da_altro_punto = math.sqrt((math.pow(abs(altro_punto.x - self.x), 2)) + (math.pow(abs(altro_punto.y - self.y), 2))) 
        return distanza_da_altro_punto
    
    def visualizza(self) -> None:
        print(f"Coordinate del punto: ({self.x},{self.y})")

class Rettangolo: 
    def __init__(self, p1: "Punto", p2: "Punto"):
        self.p1 = p1
        self.p2 = p2
    
    def base(self) -> int:
        return abs((self.p1.x - self.p2.x))
    
    def altezza(self) -> int:
        return abs((self.p1.y - self.p2.x))

    def area(self) -> float:
        return self.base() * self.altezza()
    
    def contiene(self, p: "Punto") -> bool:
        x_min = min(self.p1.x, self.p2.x)
        x_max = max(self.p1.x, self.p2.x)
        y_min = min(self.p1.y, self.p2.y)
        y_max = max(self.p1.y, self.p2.y)
        if p.x >= x_min and p.x <= x_max and p.y >= y_min and p.y <= y_max:
            return True
        else:
            return False

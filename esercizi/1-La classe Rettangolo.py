from random import randint
class Rettangolo: 
    def __init__(self, base=10, altezza=10):
        self.base = base
        self.altezza = altezza
        self.area = base * altezza

r1 = Rettangolo(randint(1, 100), randint(1, 100))
r2 = Rettangolo(randint(1, 100), randint(1, 100))
from typing import final, override
from spaceship import Spaceship

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
    
    
    


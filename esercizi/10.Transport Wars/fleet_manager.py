from spaceship import SupplyDrone

import spaceship as s

class FleetManager:
    def __init__(self):
        self.fleet = []
    
    def add_ship(self, ship) -> None:
        try:
            name = ship.name
            fuel = ship.fuel
        except AttributeError:
            raise ValueError("Object provided is not a valid ship")
        self.fleet.append(ship)

    def get_total_drone_value(self) -> int:
        value = 0
        if self.fleet == []:
            return 0
        for ship in self.fleet:
            if isinstance(ship, SupplyDrone):
                value += ship.value
        return value
    
    def get_optimal_ship(self, distance: float):
        optimal_ship = None
        highest_residual_fuel = 0
        if self.fleet == []:
            return None
        for ship in self.fleet:
            original_fuel = ship.fuel
            ship.fly(distance)
            if ship.fuel > highest_residual_fuel:
                highest_residual_fuel = ship.fuel
                optimal_ship = ship.name
            ship.fuel = original_fuel
        return optimal_ship





                




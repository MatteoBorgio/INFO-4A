from spaceships import SupplyDrone

class RebelHacker:
    def __init__(self, skill_level=1):
        if skill_level < 1 or skill_level > 5:
            raise ValueError("Skill level must be in the range 1-5")
        self.__skill_level = skill_level

    @property
    def skill_level(self):
        return self.__skill_level
    
    def manual_sort(self, drones: list[SupplyDrone]):
        for drone in drones:
            if not isinstance(drone, SupplyDrone):
                raise TypeError(f"Expected SupplyDrone, but got {type(drone)}")
        for i in range(len(drones)):
            for j in range(0, (len(drones) - i) - 1):
                if (drones[j].value / drones[j].hack_time) < (drones[j + 1].value / drones[j + 1].hack_time):
                    drones[j], drones[j + 1] = drones[j + 1], drones[j]
                
    def optimize_heist(self, drones: list[SupplyDrone], time_limit: int) -> tuple[list[SupplyDrone], int]:
        self.manual_sort(drones)
        time_spent = 0
        loot = 0
        stolen_drones = []
        for drone in drones:
            real_time = drone.hack_time * (1 - 0.10 * self.__skill_level)
            if time_limit >= time_spent + real_time:
                time_spent += real_time
                loot += drone.value
                stolen_drones.append(drone)
        
        return (stolen_drones, loot)





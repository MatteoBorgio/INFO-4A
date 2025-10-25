class Potion:
    def __init__(self, name: str, effect: str, amount: int, duration: int):
        if name == "":
            raise ValueError("Name can't be empty")
        if type(name) is not str:
            raise ValueError("Name must be a string")
        self.__name = name
        if effect not in ["heal", "buff_str", "buff_dex"]:
            raise ValueError("Effect must be heal, buff_dex or buff_str")
        self.__effect = effect
        if amount < 1:
            raise ValueError("Amount must be >= 1")
        self.__amount = amount
        if duration < 0:
            raise ValueError("Duration must be ")
        self.__duration = duration
        self.__used = False
    
    @property
    def used(self) -> bool:
        return self.__used
    
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, new_name: str) -> None:
        if new_name == "":
            raise ValueError("Name can't be empty")
        if type(new_name) is not str:
            raise ValueError("Name must be a string")
        self.__name = new_name

    @property
    def effect(self) -> str:
        return self.__effect

    @effect.setter
    def effect(self, new_effect: str) -> None:
        if new_effect not in ["heal", "buff_str", "buff_dex"]:
            raise ValueError("Effect must be heal, buff_dex or buff_str")
        self.__effect = new_effect

    @property
    def amount(self) -> int:
        return self.__amount

    @amount.setter
    def amount(self, new_amount: int) -> None:
        if new_amount < 1:
            raise ValueError("Amount must be >= 1")
        self.__amount = new_amount

    @property
    def duration(self) -> int:
        return self.__duration

    @duration.setter
    def duration(self, new_duration: int) -> None:
        if new_duration < 0:
            raise ValueError("Duration must be >= 0")
        self.__duration = new_duration

    def __apply_heal(self, target) -> int | dict:
        if hasattr(target, "heal") and callable(getattr(target, "heal")):
            return target.heal(self.__amount)
        else:
            return {"error": "unsupported_target"}
        
    def __apply_buff(self, target) -> int | dict:
        if hasattr(target, "add_buff") and callable(getattr(target, "add_buff")):
            stat = self.effect.split("_")[1]
            return target.add_buff(stat, self.__amount, self.__duration)
        else:
            return {"error": "unsupported_target"}
        
    def apply_to(self, target) -> dict:
        if self.__used:
            return {"error": "already_consumed"}
        if self.__effect == "heal":
            hp_healed = self.__apply_heal(target)
            if isinstance(hp_healed, dict):
                return hp_healed
            self.__used = True
            return {"effect": self.__effect, "amount": hp_healed, "duration": self.__duration}
        else:
            buff = self.__apply_buff(target)
            if isinstance(buff, dict):
                return buff
            self.__used = True
            return {"effect": self.__effect, "amount": buff, "duration": self.__duration}
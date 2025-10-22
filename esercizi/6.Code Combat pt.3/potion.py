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

        
from math import sqrt

class Triangle:
    def __init__(self, side_a: float, side_b: float, side_c: float):
        self.__side_a = side_a
        self.__side_b = side_b
        self.__side_c = side_c

    def calculate_area(self) -> float:
        semi_perimeter = (self.__side_a + self.__side_b + self.__side_c) / 2
        area = sqrt(semi_perimeter * (semi_perimeter - self.__side_a) * (semi_perimeter - self.__side_b) * (semi_perimeter - self.__side_c))
        return area

    def calculate_perimeter(self) -> float:
        return self.__side_a + self.__side_b + self.__side_c

    def classify_triangle(self) -> str:
        if self.__side_a == self.__side_b and self.__side_b == self.__side_c:
            return "Equilateral"
        elif self.__side_a != self.__side_b and self.__side_b != self.__side_c and self.__side_a != self.__side_c:
            return "Scalene"
        else:
            return "Isosceles"

    def __str__(self):
        return f"Lato A: {self.__side_a}; Lato B: {self.__side_b}; Lato C: {self.__side_c}"


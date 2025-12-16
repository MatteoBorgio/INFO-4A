class Student:
    def __init__(self, surname: str, name: str, tax_code: str, matriculation_number: int):
        self.__surname = surname
        self.__name = name
        self.__tax_code = tax_code
        self.__matriculation_number = matriculation_number

    @property
    def surname(self):
        return self.__surname

    @property
    def name(self):
        return self.__name

    @property
    def tax_code(self):
        return self.__tax_code

    @property
    def matriculation_number(self):
        return self.__matriculation_number

    def __str__(self):
        return f"{self.__name} {self.__surname}; Tax code: {self.__tax_code}; Matriculation_number: {self.__matriculation_number}"

if __name__ == "__main__":
    student = Student("Rossi", "Mario", "RSSMRA80A01H501U", 1)
    print(student)
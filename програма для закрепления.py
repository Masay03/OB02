class Car:
    def __init__(self, make, model): #конструктор
        self.public_make = make #открытый
        self._protected_model = model #защищенный
        self.__private_year = 2022 #приватный

    def public_method(self):
        return f"Это открытый метод. Имя создателя: {self.public_make}"

    def _protected_method(self):
        return f"Это защищенный метод. Модель: {self._protected_model}"

    def __private_method(self):
        return f"Это приватный метод. Год выпуска: {self.__private_year}"

class ElectricCar(Car):
    def __init__(self, make, model, battery_size):
        self.battery_size = battery_size
        super().__init__(make, model)

    def get_details(self):
        details = f"{self.public_make} {self._protected_model}, battery size: {self.battery_size}"
        return details

tesla = ElectricCar("Tesla", "Model S", 75)

print(tesla.get_details())
print(tesla.public_method())
print(tesla._protected_method())
print(tesla._Car__private_method())

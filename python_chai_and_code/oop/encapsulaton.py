class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
    # getter method
    def get_brand(self):
        return self.__brand + "!"

    # add a method to the car class to display the full name of car (brand and model)
    def full_name(self):
        return f"{self.__brand}-{self.model}"
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

MyCar = ElectricCar("Tata", "ElectricPunch","85kWh")
# print(MyCar._Car__brand)-->attribute convert public to private 
# and it become __brand -> _Car__brand
print(MyCar.model)
print(MyCar.battery_size)
print(MyCar.get_brand())
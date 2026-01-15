class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    # add a method to the car class to display the full name of car (brand and model)
    def full_name(self):
        return f"{self.brand}-{self.model}"
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

MyCar = ElectricCar("Tata", "ElectricPunch","85kWh")
print(MyCar.brand)
print(MyCar.model)
print(MyCar.battery_size)
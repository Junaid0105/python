class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
    # getter method
    def get_brand(self):
        return self.__brand + "!"
    # add a method to the car class to display the full name of car (brand and model)
    # def full_name(self):
    #     return f"{self.__brand}-{self.model}"
    
    ### ploymorphism - 
    def fuel_type(self):
        return "petrol or diesel"
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    def fuel_type(self):
        return "Electric charge"

MyCar = ElectricCar("Tata", "ElectricPunch","85kWh")
print(MyCar.fuel_type())
# print(MyCar._Car__brand)-->attribute convert public to private 
### and it become __brand -> _Car__brand
# print(MyCar.model)
# print(MyCar.battery_size)
# print(MyCar.get_brand())
my_car = Car("Tata", "Safari")
print(my_car.fuel_type())
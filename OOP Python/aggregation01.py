class customer:
    def __init__(self, name, gender, address):
        self.name = name
        self.gender = gender
        self.address = address
class adress:
    def __init__(self, street, city, state, country):
        self.street = street
        self.city = city
        self.state = state
        self.country = country
add = adress("1234", "Amroha", "UP", "India")
cust = customer("Junaid","male",add)
print(cust.address.country)
print(cust.address.street)
print(cust.address.city)
class Engine:
    def __init__(self, horsepower, type):
        self.horsepower = horsepower
        self.type = type

class Car:
    def __init__(self, make, model, engine):
        self.make = make
        self.model = model
        self.engine = engine

engine = Engine(300, "V6")
car = Car("Toyota", "Camry", engine)

print(car.engine.horsepower)
print(car.engine.type)

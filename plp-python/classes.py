class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descrptive_name(self):
        return f"{self.year} {self.make.title()} {self.model.title()}"
    
    def fill_gas_tank(self):
       return("Gas tank is now full.")

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)


    def fill_gas_tank(self):
        return("This car doesn't need a gas tank!")

#  Instances of the classes
car1 = Car("Toyota", "Corolla", 2020)
car2 = ElectricCar("Tesla", "Model S", 2022)

print(car1.get_descrptive_name())
print(car2.get_descrptive_name())

for need_gas in [car1, car2]:
    print(f"{need_gas.model} {need_gas.fill_gas_tank()}")
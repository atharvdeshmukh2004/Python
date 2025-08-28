"""
1. Basic Class and Object
Problem: Create a Car class with attributes like __brand and __model. Then create an instance of this class.
        
2. Class Method and Self
Problem: Add a method to the Car class that displays the full name of the car (__brand and __model).

3. Inheritance
Problem: Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.

4. Encapsulation
Problem: Modify the Car class to encapsulate the __brand attribute, making it private, and provide a getter method for it.

5. Polymorphism
Problem: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.

6. Class Variables
Problem: Add a class variable to Car that keeps track of the number of cars created.

7. Static Method
Problem: Add a static method to the Car class that returns a general description of a car.

8. Property Decorators
Problem: Use a property decorator in the Car class to make the __model attribute read-only.

9. Class Inheritance and isinstance() Function
Problem: Demonstrate the use of isinstance() to check if my_tesla is an instance of Car 

10. Multiple Inheritance
Problem: Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance"
"""

class Car:
    total_car = 0

    def __init__(self,__brand,__model):
        self.__brand = __brand
        self.__model = __model
        Car.total_car += 1

    def full_name(self):
        return f"{self.__brand} {self.__model}"  
    
    @property
    def get_brand(self):
        return self.__brand
    
    def full_type(self):
        return "Disele or Petrol"
    
    @property
    def get_model(self):
        return self.__model
    
    def general_description():
        return "Cars are means of transportation"
    


class ElectricCar(Car):
    def __init__(self, __brand, __model , battry_size):
        super().__init__(__brand, __model)
        self.battry_size = battry_size

    def full_type(self):
        return "Electricity"    

my_car = Car("Lamborghini","Urus")
car = ElectricCar("Tata","Curve","90KWh")


# print(isinstance(car,Car))
# print(isinstance(car,ElectricCar))

class Engine:
    def engineInfo(self):
        return "This is v8 Engine"

class Battery:
    def batteryInfo(self):
        return "This uses 120KWh Battery"

class ElectricVehicle(Engine,Battery):
    pass

car1 = ElectricVehicle()
print(car1.engineInfo())
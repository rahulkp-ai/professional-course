class Vehicle:
    wheels = 4

    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def description(self):
        return f"The {self.make} {self.model}"

car = Vehicle("BMW", "i3")

print(car.wheels)
print(car.description())

class Pet:
    def eat(self):
        print("Chomp")

class Dog(Pet):
    def bark(self):
        print("Bark...!")

dog = Dog()
dog.eat()
dog.bark()


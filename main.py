#python classes

class Dog():
    #initialize the attributes on the
    #shiny new object
    def __init__(self, name, age=0):
        self.name= name
        self.age=age

    def bark(self):
        print(f"{self.name} say woof!")

    def __str__(self):
        return f'Dog named {self.name} is {self.age} years young'

spot = Dog('Spot', 8)
dog = Dog('Lassie')

print(spot)
print(dog)
print(spot.age)

class Vehicle():

    def __init__(self, make, model, running=False):
        self.make=make
        self.model=model
    
    def start(self):
        running=True
        print('running...')

    def stop(self):
        running=False
        print('stopped...')

    def __str__(self):
        return f"Vehicle is a {self.make} model {self.model}"
    
car= Vehicle('ford', "fiesta")

print(car)
# Base class
class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city

    def introduce(self):
        print(f"I am {self.name}, protector of {self.city}!")
    
    def use_power(self):
        print(f"{self.name} uses their power of {self.power}!")

# Subclass with inheritance & polymorphism
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, city, flight_speed):
        super().__init__(name, power, city)
        self.flight_speed = flight_speed  # unique attribute for flying heroes

    # Overriding use_power method to include flying
    def use_power(self):
        print(f"{self.name} flies at {self.flight_speed} mph while using {self.power}!")

    def fly(self):
        print(f"{self.name} is soaring through the skies of {self.city}!")

# Creating instances
hero1 = Superhero("MightyMan", "Super Strength", "Metro City")
hero2 = FlyingSuperhero("SkyWing", "Laser Eyes", "Cloudville", 300)

# Using the methods
hero1.introduce()
hero1.use_power()

print("---")

hero2.introduce()
hero2.use_power()
hero2.fly()

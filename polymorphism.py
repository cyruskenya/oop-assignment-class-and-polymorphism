class Car:
    def move(self):
        print("Driving 🚗")

class Plane:
    def move(self):
        print("Flying ✈️")

class Boat:
    def move(self):
        print("Sailing ⛵")

def start_moving(vehicle):
    vehicle.move()

# Create instances
my_car = Car()
my_plane = Plane()
my_boat = Boat()

# Call move() using the same interface
start_moving(my_car)    # Driving 🚗
start_moving(my_plane)  # Flying ✈️
start_moving(my_boat)   # Sailing ⛵


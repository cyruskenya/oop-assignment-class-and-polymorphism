What’s happening here?

Superhero is the base class with basic attributes like name, power, and city.

The introduce() and use_power() methods describe the hero.

FlyingSuperhero inherits from Superhero, adding flight_speed.

It overrides use_power() to include flying speed info (polymorphism).

It also adds a new method fly().

Each object is initialized with unique data via the constructor (__init__).

How polymorphism works:

Each class defines its own move() method.

The start_moving() function accepts any object and calls move()—showing polymorphism in action.

The same method name behaves differently depending on the object.

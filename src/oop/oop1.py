# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# Base Class
class Vehicle:
    pass

# Base Flight Class
class FlightVehicle(Vehicle):
    pass

# Flight Child
class Starship(FlightVehicle):
    pass

# Flight Child
class Airplane(FlightVehicle):
    pass

# Base Ground Class
class GroundVehicle(Vehicle):
    pass

# Ground Child
class Car(GroundVehicle):
    pass

class Motorcycle(GroundVehicle):
    pass

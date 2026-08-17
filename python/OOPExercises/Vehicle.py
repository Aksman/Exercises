# EXERCISE
# Create a Vehicle class with a color property "White".
# Change the color property of the class itself, and observe 
# that its instances also change color.

class Vehicle:
    color = 'white'
    speed = 200

    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model

    # __str__() is a "dunder" method you can set up in any class to give 
    # the parser instructions on how to represent it as a string.
    def __str__(self):
        return f"{self.make} {self.model} -- color: {self.color}, top speed: {self.speed}"

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    tesla = Vehicle('Tesla', 'Model S')
    toyota = Vehicle('Toyota', 'Carolla')
    honda = Vehicle('Honda', 'Accord')

    # Change the color of one vehicle
    toyota.color = 'blue'

    # Because we're defined how to represent the class as a string through the __str__()
    # method, this works.
    print(tesla)
    print(toyota)
    print(honda)

    # Change the default color of the Vehicle class and observe how its instances change

    Vehicle.color = 'red'
    # The colors of tesla and honda should change. Because we set the color of toyota to 
    # something else, it remains the color we set it.
    print(tesla)
    print(toyota)
    print(honda)



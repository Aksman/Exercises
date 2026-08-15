# EXERCISE
# Create a Lamp class. It should have two states, OFF and ON, and a switch method that toggles between the two.

class Lamp:
    # Always initialize a Lamp to be unlit. Note the use of the double-underscore prefix
    # to make the property private, preventing the property from being set externally.
    def __init__(self):
        self.__lit = False

    # Toggle the state, making it the opposite boolean state than it was.
    def switch(self):
        self.__lit = not self.__lit

    # Create a public view of the lit property, which translates the internal True/False 
    # status to 'ON' or 'OFF'.
    @property
    def lit(self):
        return 'ON' if self.__lit else 'OFF'

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    frageelay = Lamp()
    print(f"The lamp is {frageelay.lit}.")
    frageelay.switch()
    print(f"Now the lamp is {frageelay.lit}.")
    frageelay.switch()
    print(f"Now the lamp is {frageelay.lit}.")

# EXERCISE
# Create a Temperature class that stores a temperature as Celsius.
# There should be methods to output the temperature expressed in several different scales,
# and a method to change the temperature based on several different scales.

class Temperature:
    # Note the use of the double underscore prefix ('__') to make the temperature property private.
    def __init__(self, temperature: float = 37.0):
        self.__temperature = temperature

    # Internal storage is in Celsius
    def asCelsius(self) -> float:
        return self.__temperature

    def asFahrenheit(self) -> float:
        return self.__temperature * 1.8 + 32

    def asKelvin(self) -> float:
        return self.__temperature + 273.15

    def asRankine(self) -> float:
        return self.__temperature * 1.8 + 491.67

    def setTemperature(self, value: float, scale: str = 'C'):
        if scale.lower() in ['c', 'celsius', 'centigrade']:
            self.__temperature = value
        elif scale.lower() in ['f', 'fahrenheit']:
            self.__temperature = (value - 32) * 5/9 
        elif scale.lower() in ['k', 'kelvin']:
            self.__temperature = value - 273.15
        elif scale.lower() in ['r', 'rankine']:
            self.__temperature = (value - 491.67) * 5/9

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    import sys
    temp = float(sys.argv[1]) if len(sys.argv) > 1 else 37.0
    t = Temperature(temp)

    print(f"Celsius: {t.asCelsius()} C")
    print(f"Fahrenheit: {t.asFahrenheit()} F")
    print(f"Kelvin: {t.asKelvin()} K")
    print(f"Rankine: {t.asRankine()} R")

    t.setTemperature(100)

    print("\nNew Temperature\n")
    print(f"Celsius: {t.asCelsius()} C")
    print(f"Fahrenheit: {t.asFahrenheit()} F")
    print(f"Kelvin: {t.asKelvin()} K")
    print(f"Rankine: {t.asRankine()} R")
    

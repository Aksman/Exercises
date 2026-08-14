# EXERCISE
# Create a Rectangle class with length and height properties, and with
# methods that return the perimeter and area.

class Rectangle:
    def __init__(self, length: int|float, height: int|float):
        self.length = length
        self.height = height

    def area(self):
        return self.length * self.height

    def perimeter(self):
        return 2 * (self.length + self.height)

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    def convertNumber(text: str) -> int|float:
        try:
            return int(text)
        except:
            try:
                return float(text)
            except:
                raise ValueError('Invalid numeric string.')

    import sys
    length = convertNumber(sys.argv[1]) if len(sys.argv) > 1 else 5
    height = convertNumber(sys.argv[2]) if len(sys.argv) > 2 else 2

    print(f"Rectangle: {length} x {height}")
    r = Rectangle(length, height)
    print(f"Perimeter: {r.perimeter()}")
    print(f"Area: {r.area()}")
# EXERCISE
# Create a Vector class representing a two-dimensional vector. Allow a programmer 
# to add two Vectors together using the "+" operator.

class Vector:
    def __init__(self, x: int|float, y: int|float):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    v1 = Vector(3, 4)
    v2 = Vector(2, 5)
    # Vector addition as we defined
    v3 = v1 + v2

    # String representation as we defined
    print(f"{v1} + {v2} = {v3}")

    # Object representation as we defined
    print(f"{repr(v1)} added to {repr(v2)} to create {repr(v3)}")
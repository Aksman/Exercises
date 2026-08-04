# EXERCISE
# Create a function that returns both the sum and difference of two numbers.
# This demonstrates how to return multiple values in a function.

# Note that the returned value is a tuple, even though in code we handle it
# as two separate values separated by a comma.
def sumAndDiff(num1: int|float, num2: int|float) -> tuple[int|float]:
    return num1 + num2, num1 - num2

# Example usage
# This block runs only when this script is accessed directly (i.e. not imported).
if __name__ == '__main__':
    first = int(input('Enter the first number: '))
    second = int(input('Now the second number: '))
    s, d = sumAndDiff(first, second)
    print(f"Sum: {s}")
    print(f"Diff: {d}")
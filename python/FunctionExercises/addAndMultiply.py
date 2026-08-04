# EXERCISE
# Calculate both a triangular number and a factorial of a number.
# This example will demonstrate a higher-order function.

def triangularNumber(number: int) -> int:
    triNum = 0
    for i in range(1, number + 1):
        triNum += i
    return triNum

def factorial(number: int) -> int:
    if number in [0, 1]:
        return 1
    else:
        f = 1
        for i in range(2, number + 1):
            f *= i
        return f

def doIt(func, a):
    return func(a)

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    import sys
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    print(f"Triagular: {doIt(triangularNumber, n)}")
    print(f"Factorial: {doIt(factorial, n)}")
    

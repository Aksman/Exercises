# EXERCISE
# Create a function to calculate a factorial 

def factorial(num: int) -> int:
    if num < 0:
        return ValueError('Factorial not defined for negative numbers.')
    if num == 0 or num == 1:
        return 1
    else:
        result = 1
        for i in range(2, num + 1):
            result *= i
        return result
    

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    num = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    print(f"{num}! = {factorial(num)}")

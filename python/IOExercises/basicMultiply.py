# EXERCISE
# Accept two numbers from the user and return their product.
# This exercise demonstrates basic command line IO, plus conversion from string input.

def basicMultiplyIO():

    # Use input() to get command line input. Notice the use of int() to convert
    # the user input into an integer. By default, input() returns a string.
    factor1 = int(input('Please input the first integer: '))
    factor2 = int(input('Now input the second integer: '))
    product = factor1 * factor2
    print(f"The answer is {product}.")

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    basicMultiplyIO()
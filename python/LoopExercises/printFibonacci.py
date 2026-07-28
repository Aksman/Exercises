# EXERCISE
# Create a function that prints out the first several numbers in a Fibonacci sequence.
#
# A Fibonacci sequence begins with 0 and 1, then every subsequent number is the sum of the 
# two numbers before it.
def printFibonacci(limit: int):

    # Negative numbers are not allowed.
    if limit < 0:
        raise ValueError('Negative numbers not allowed.')
    
    # Initialize the first two numbers
    n1 = 0
    n2 = 1

    # Loop through each of the numbers. Recall that the range function is inclusive at the start
    # and exclusive at the end. If limit = 10, then the range will be from 1 to 10.
    for i in range(1, limit + 1):

        # Explicitly return the first two numbers.
        if i == 1:
            print('0 ', end='')
        elif i == 2:
            print('1 ', end='')
        else:
            # Add the two previous numbers to find the next in the sequence
            n = n1 + n2
            # Print it
            print(f"{n} ", end='')
            # Set the two previous numbers for the next in the sequence.
            n1 = n2
            n2 = n

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    printFibonacci(limit)
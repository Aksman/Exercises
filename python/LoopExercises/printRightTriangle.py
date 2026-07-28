# EXERCISE
# Create a function that prints a right triangle using sequences of integers of increasing length.
# The output should look something like this:
#
# 1
# 1 2
# 1 2 3
# The reverse flag prints the triangle upside down, like this:
#
# 1 2 3
# 1 2
# 1

def printRightTriangleSequences(limit: int, reverse: bool = False):
    if limit <= 0:
        raise ValueError('Only positive integers allowed.')
    # Determine the width needed
    width = len(str(limit))
    myRange = range(limit, 0, -1) if reverse else range(1, limit + 1)
    for i in myRange:
        for j in range(1, i + 1):
            # Braces within braces allows us to format based on a variable.
            # ":<{width}" tells us to right-justify in a string of the length we 
            # determined we needed in line 13.
            print(f"{j:<{width}} ", end='')
        print('') # Default ending is a new line

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    printRightTriangleSequences(limit, True)
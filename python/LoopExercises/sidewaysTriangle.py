# EXERCISE 
# Create a function that prints a triangle of a particular character
# where the lines increase then decrease in length.
#
# Example:
#
# *
# **
# ***
# **
# *

def printSidewaysTriangle(char: str = '*', size: int = 5):
    for i in range(1, size + 1):
        print(char * i)
    for j in range(size - 1, 0, -1):
        print(char * j)

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    char = sys.argv[1] if len(sys.argv) > 1 else '*'
    limit = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    printSidewaysTriangle(char, limit)
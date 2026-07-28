# EXERCISE
# Print a hollow square made up of stars with the character and size specified

def printHollowSquare(char: str = '*', size: int = 5):
    print(char * size)
    for i in range(2, size):
        print(char + (' ' * (size - 2)) + char)
    print(char * size)

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    char = int(sys.argv[1]) if len(sys.argv) > 1 else '*'
    limit = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    printHollowSquare(char, limit)
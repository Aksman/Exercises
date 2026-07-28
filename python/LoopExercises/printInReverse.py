# EXERCISE
# Print a list in reverse order.

# This version of the function uses the reversed() function.
def printInReverse1(listing: list):
    for item in reversed(listing):
        print(item)

# This version of the function uses Python list slicing with the -1 step parameter.
def printInReverse2(listing: list):
    for item in listing[::-1]:
        print(item)

# This version uses a custom range from the length of the listing - 1 to 0, stepping in reverse.
def printInReverse3(listing: list):
    for i in range(len(listing) - 1, -1, -1):
        print(listing[i])

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    myList = sys.argv[1:] if len(sys.argv) > 1 else range(10, 101, 10)
    printInReverse3(myList)
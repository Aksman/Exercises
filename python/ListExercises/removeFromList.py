# EXERCISE
# Create a function that removes every item from a list that is a specified value.

def removeFromList(elements: list, value) -> list:
    # We use a list comprehension instead of a loop 
    # to create a list without the specified value
    return [el for el in elements if el != value]

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    import sys
    removalValue = sys.argv[1] if len(sys.argv) > 1 else 6
    myList = sys.argv[2:] if len(sys.argv) > 2 else [1, 5, 6, 2, 6, 7, 8, 6, 3]

    print(f"Original: {myList}")
    print(f"Processed: {removeFromList(myList, removalValue)}")
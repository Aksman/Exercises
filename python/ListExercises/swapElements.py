# EXERCISE
# Create a function that swaps two elements in a list 

# The function takes a list and two indexes, and returns the altered list.
def swap2(lst: list, index1: int, index2: int) -> list:
    # We're doing this so it preserves the original list by default
    result = lst.copy()

    # Swap the elements
    # Note the use of Pythons comma notation to handle multiple variables at once
    result[index1], result[index2] = result[index2], result[index1]

    return result

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    import sys
    index1 = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    index2 = int(sys.argv[2]) if len(sys.argv) > 2 else 2
    myList = sys.argv[3:] if len(sys.argv) > 3 else [1, 2, 3, 4]
    print(f"Original List: {myList}")
    newList = swap2(myList, index1, index2)
    print(f"New List: {newList}")
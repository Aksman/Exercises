# EXERCISE
# Test if a list is sorted.
# The tempting thing is to create a sorted version of the list and compare. But 
# sorting is a complex operation, while testing whether a list is sorted should
# only require one pass through.

def isSorted(lst: list) -> bool:
    # Use the all() function with a generator expression to determine
    # whether every element is <= the element after it.
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    import sys
    myList = sys.argv[1:] if len(sys.argv) > 1 else [1, 3, 5, 6, 7, 9, 12, 14]
    print(f"The List: {myList}")
    print(f"Is it sorted? {'Yes' if isSorted(myList) else 'No'}.")
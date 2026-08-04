# EXERCISE
# Demonstrate a few basic operations on a list.

def basicOperations(lst: list) -> tuple:
    # Operation #1: Return the third element in the list
    # Return None if there is no third element.
    if len(lst) < 3:
        third = None
    else:
        # The index of the first element is 0.
        third = lst[2]

    # Operation #2: Return the number of elements in the list
    length = len(lst)

    # Operation #3: Return if the list is empty
    isEmpty = length == 0

    # Return all the results
    return third, length, isEmpty

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    import sys
    myList = sys.argv[1:] if len(sys.argv) > 1 else ['first', 'second', 'third', 'fourth', 'fifth']
    third, size, isEmpty = basicOperations(myList)
    print(f"Third element: {third}")
    print(f"Size of list: {size}")
    print(f"Is it Empty? {'Yes' if isEmpty else 'No'}")
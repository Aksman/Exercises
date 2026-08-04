# EXERCISE
# Reverse the order of a list.

def manualReverse(elements: list) -> list:
    # Initialize our list
    result = []

    # This steps backward through the elements of the list.
    # For a four element list, it will cover indexes -1 through -4, 
    # stopping before it reaches -5.
    for i in range(-1, -len(elements) - 1, -1):
        result.append(elements[i])

    return result


def manualReverseDestructive(elements: list) -> list:
    # Initialize our list
    result = []

    # Cycle through popping off the last element of the list
    # and adding it to the result list. Stop when the original 
    # list is empty.
    while len(elements) > 0:

        # The .pop() method can take an index, but by default
        # it's -1, i.e. the last element. It also removes said
        # element from the original list.
        el = elements.pop()
        result.append(el)

    return result

    
# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    import sys
    myList = sys.argv[1:] if len(sys.argv) > 1 else [1, 2, 3, 4, 5]

    copiedList = myList.copy()
    print(f"List: {copiedList}")

    # Slicing creates a new list, and does not affect the original
    reversedList = copiedList[::-1]
    print(f"Reversed By Slicing: {reversedList}")
    print(f"Original List: {copiedList}")

    # The .reverse() method modifies the original list
    copiedList.reverse()
    print(f"Now permanently reversed: {copiedList}")

    reversedList2 = manualReverse(myList)
    print(f"Reversed manually: {reversedList2}")
    print(f"Original List: {myList}")

    reversedList3 = manualReverseDestructive(myList)
    print(f"Reversed manually in a destructive manner: {reversedList3}")
    print(f"Original List: {myList}")

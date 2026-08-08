# EXERCISE
# Create a function that inserts a new value in a list after a particular value.
# If the value is not found, it appends it.

def insertAfter(elements: list, search, insert) -> list:
    # Create a copy so that we return a new list and don't
    # modify the existing list.
    result = elements.copy()

    try:
        found = result.index(search)
        result.insert(found + 1, insert)
    except:
        result.append(insert)

    return result

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    myList = ['The', 'quick', 'brown', 'fox', 'jumps', 'the', 'lazy', 'dog']
    newList = insertAfter(myList, 'jumps', 'over')
    print(newList)

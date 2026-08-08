# EXERCISE
# Create a function that finds the first occurence of a specific value in a list, 
# replace it with another, and return the altered list.

def findAndReplace(elements: list, search, replace) -> list:
    result = elements.copy()
    try:
        i = result.index(search)
        result[i] = replace
    except:
        # Do nothing if not found
        pass
    return result

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    myList = ['The', 'quick', 'brown', 'fox', 'jumps', 'under', 'the', 'lazy', 'dog']
    newList = findAndReplace(myList, 'under', 'over')
    print(newList)
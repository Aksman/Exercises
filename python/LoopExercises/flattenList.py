# EXERCISE
# Create a function that "flattens" a list, i.e. turns a multi-dimensional list 
# into a one-dimensional one.

def flatten(items: list) -> list:
    result = []
    for item in items:
        if type(item) == list:
            item = flatten(item)
            result += item
        else:
            result += [item]
    return result

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    myList = sys.argv[1:] if len(sys.argv) > 1 else [[1, 2], [3, 4, [5, 6], 7], [[8, 9], 10]]
    print(flatten(myList))
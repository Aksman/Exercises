# EXERCISE
# Find a number hidden in a map and return the coordinates.
# The "map" is a two-dimensional nested list structure.

def findInMap(needle, haystack: list[list]) -> tuple:
    # Use enumerate() to loop through the outer list 
    # with easy access to both the index (x-coord.)
    # and the inner lists.
    for x, lst in enumerate(haystack):
        # Again use enumerate for easy access to 
        # the index (y-coord.) and the value.
        for y, val in enumerate(lst):
            if val == needle:
                return (x, y)

    # Not found
    return (None, None)

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import ast
    import sys
    gem = sys.argv[1] if len(sys.argv) > 1 else 60
    myMap = ast.literal_eval(sys.argv[2]) if len(sys.argv) > 2 else [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
    x, y = findInMap(gem, myMap)
    if x is not None:
        print(f"{gem} is found at ({x}, {y}).")
    else:
        print(f"{gem} was not found.")
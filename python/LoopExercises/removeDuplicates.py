# EXERCISE
# Create a function to remove duplicates

# Use sets
def removeDuplicates1(elements: list) -> list:
    # Convert to a set (a collection type that does not allow duplicates) then back into a list.
    return list(set(elements))

# Using a loop
def removeDuplicates2(elements: list) -> list:
    uniques = {}
    for el in elements:
        uniques[el] = True

    # Using list() to convert a dict returns a list of the keys, discarding the values.
    # uniques.keys() would accomplish the same thing.
    return list(uniques)

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    myList = sys.argv[1:] if len(sys.argv) > 1 else [1, 1, 2, 2, 2, 3, 4, 5, 4, 5, 5, 6]
    uniques1 = removeDuplicates1(myList)
    print(f"Method #1: {uniques1}")
    uniques2 = removeDuplicates2(myList)
    print(f"Method #2: {uniques2}")
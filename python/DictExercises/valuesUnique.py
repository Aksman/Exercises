# EXERCISE
# Create a function that determines if a dictionary's values are all unique.

def valuesUnique(data: dict) -> bool:
    # Use the .values() method to extract a list of values from the dictionary.
    # (This is actually a view object, so use list() to turn it into an actual list.)
    # A Python set is a construct that forces all values to be unique. Convert the list
    # into a set and compare it to the list. If all the values are unique, the list
    # and set will be the same size.
    values = list(data.values())
    return len(values) == len(set(values))

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    data1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
    data2 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 2}

    print(f"Is the first data set unique? {'Yes' if valuesUnique(data1) else 'No'}.")
    print(f"Is the second data set unique? {'Yes' if valuesUnique(data2) else 'No'}.")
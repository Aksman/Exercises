# EXERCISE
# Create a function that finds what keys two dictionaries have in common.

def commonKeys(dict1: dict, dict2: dict) -> list:
    # Three things going on here: 1. the .keys() method on the dictionaries, which returns
    # a dynamic view object of the keys in the dictionary. 2. The '&' operator creates an intersection
    # between the two views as a set. 3. The list() function converts the resulting set into a list.
    return list(dict1.keys() & dict2.keys())

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    dict1 = {'a': 1, 'b': 2, 'c': 3}
    dict2 = {'b': 1, 'c': 2, 'd': 3, 'e': 4}

    print(commonKeys(dict1, dict2))
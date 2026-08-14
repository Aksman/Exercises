# EXERCISE
# Create a function that takes two dictionaries and returns a list of keys
# that exist in the first but not in the second.

def diffKeys(dict1: dict, dict2: dict) -> list:
    # Three things going on in this one line
    # 1. Using the .keys() dictionary method to return a dictionary view of its keys.
    # 2. Using the set difference operator ('-') to create a set of keys in the first that are not in the second.
    # 3. Using the list() function to convert the resulting set into a list.
    return list(dict1.keys() - dict2.keys())

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    dict2 = {'b': 1, 'd': 2, 'f': 3}

    print(f"Difference: {diffKeys(dict1, dict2)}")
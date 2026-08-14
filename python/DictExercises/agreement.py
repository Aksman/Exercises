# EXERCISE
# Create a function that compares two dictionaries and returns a dictionary where the keys and values
# in both dictionaries are identical.

# Method #1: Convert dictionaries into sets of tuples using the items() method,
#  take the intersection, and convert back into a dictionary.
def agreement(dict1: dict, dict2: dict) -> dict:
    return dict(dict1.items() & dict2.items())

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    dict2 = {'a': 1, 'b': 3, 'c': 5, 'd': 4, 'e': 2}

    print(f"Agreement: {agreement(dict1, dict2)}")
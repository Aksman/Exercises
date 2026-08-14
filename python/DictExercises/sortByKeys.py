# EXERCISE
# Create a function that sorts a dictionary according to keys.

def sortByKeys(data: dict) -> dict:
    # The .items() method returns a view object that produces a
    # list of tuples of the dictionaries key-value pairs. sorted()
    # sorts this list of tuples by the first value, i.e the key.
    # The dict function turns this list of tuples back into a dictionary.
    return dict(sorted(data.items()))

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    inventory = {
        'dates': 12,
        'apples': 42,
        'cherries': 61,
        'bananas': 35,
    }

    sortedInv = sortByKeys(inventory)
    print(sortedInv)
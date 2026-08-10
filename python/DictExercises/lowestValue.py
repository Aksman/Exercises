# EXERCISE
# Create a function that returns the key that has the lowest value in a dictionary

# Method #1: Classic algorithm
def lowestValueKey1(data: dict):
    lowestKey = None
    lowestValue = None
    for k, v in data.items():
        if lowestValue is None or v < lowestValue:
            lowestKey = k
            lowestValue = v
    return lowestKey

def lowestValueKey2(data: dict):
    # Applying get method of the data dictionary to the key argument for min()
    # makes the min() function search for the lowest value.
    return min(data, key=data.get)

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    inventory = {
        'apples': 40,
        'bananas': 50,
        'cherries': 140,
        'grapes': 61,
        'lemons': 22,
        'pears': 57
    }

    print(f"Lowest inventory (Method #1): {lowestValueKey1(inventory)}")
    print(f"Lowest inventory (Method #2): {lowestValueKey2(inventory)}")
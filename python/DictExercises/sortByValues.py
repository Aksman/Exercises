# EXERCISE
# Create a function that sorts a dictionary by its values.

def sortByValue(data: dict) -> dict:
    # We use the .items() dictionary method to produce (essentially) 
    # a list of tuples representing the key-value pairs. The key argument
    # in the sorted function uses a lamba function to look at the second
    # (index 1) item in each tuple, which corresponds to the value, and
    # sorts according to that. Finally the dict() function takes the 
    # sorted list of tuples and turns it back into a dictionary.
    return dict(sorted(data.items(), key=lambda x: x[1]))

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    inventory = {
        'dates': 12,
        'apples': 42,
        'cherries': 61,
        'bananas': 35,
    }

    sortedInv = sortByValue(inventory)
    print(sortedInv)
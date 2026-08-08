# EXERCISE
# Create a function that uses a list of keys and list of values 
# and creates a dictionary.

def zipDict(keys: list, values: list) -> dict:
    # zip() converts the two lists into a list of tuples.
    # dict() then converts this list of tuples into a dictionary.
    return dict(zip(keys, values))

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    keys = ['name', 'age', 'city']
    vals = ['Avery Anderson', 27, 'Atlanta']
    myDict = zipDict(keys, vals)
    print(myDict)
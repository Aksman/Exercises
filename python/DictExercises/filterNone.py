# EXERCISE
# Create a function that filters out all entries in a dictionary with a value of None.

def filterNone(data: dict) -> dict:
    # A dictionay comprehension expression makes this very easy in Python
    # Notice we need to use the .items() method, which returns a dictionary's
    # key-value pairs as tuples.
    return {key: value for key, value in data.items() if value is not None}

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    data = {
        'name': 'David',
        'age': None,
        'city': 'Atlanta',
        'state': 'GA',
        'zip': None
    }

    print(f"Unfiltered: {data}")
    print(f"Filtered: {filterNone(data)}")
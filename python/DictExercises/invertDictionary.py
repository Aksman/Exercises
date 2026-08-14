# EXERCISE
# Create a function that "inverts" a dictionary, where the keys become values and the values
# become keys. In the case where values are repeated, put all the keys into a list.

def invertDict(data: dict) -> dict:
    # Initialize our dictionary
    result = {}
    # Loop through key-value pairs
    for key, value in data.items():
        # The .setdefault method returns the value at the specified key, or inserts a value 
        # into the dictionary and returns it if not found. The effect here is that we either 
        # append the key to the list, or initialize to an empty list and then append.
        result.setdefault(value, []).append(key)
    return result

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    data = {'a': 1, 'b': 2, 'c': 3, 'd': 2, 'e': 5, 'f': 2, 'g': 3, 'h': 1}
    print(f"Inverted: {invertDict(data)}")
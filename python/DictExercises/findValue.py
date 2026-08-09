# EXERCISE
# Create a function that return whether or not a value can be found in a dictionary.

def valueFound(data: dict, value) -> bool:
    # "value in data" will return if the value is found in the dictionary's keys.
    # If you want to look in the values, use the values() method to return a list
    # of its values.
    return value in data.values()

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    roles = {
        'publisher': 'J Jonah Jameson', 
        'editor': 'Joe Robertson', 
        'reporter': 'Ned Leeds', 
        'photographer': 'Peter Parker',
        'secretary': 'Betty Brant'
    }

    lookup = ['Peter Parker', 'Steve Rogers', 'Betty Brant']
    print("Do they work for the Daily Bugle?")
    for l in lookup:
        print(f"{l}: {'Yes' if valueFound(roles, l) else 'No'}.")
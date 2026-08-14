# EXERCISE
# Create a function that returns the key with the highest value.

def highestValue(data: dict):
    # Setting the key parameter to "data.get" instructs the max() function to 
    # make its comparison based on the .get() method on the data dict.
    return max(data, key=data.get)

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    grades = {
        'Avery Anderson': 96,
        'Brian Bates': 98,
        'Christina Calloway': 69,
        'David Dixon': 77,
        'Ellie Edwards': 93,
        'Frank Fisher': 83,
        'Georgina Guerrero': 97
    }

    print(f"Highest score: {highestValue(grades)}")
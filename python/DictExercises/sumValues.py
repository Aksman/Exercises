# EXERCISE
# Create a function that finds the sum of values in a dictionary
#

def sumValues(data: dict) -> int|float:
    # This is made easy by the .values() method for dictionaries, 
    # which returns a list of its values, and the sum() function,
    # which finds the sum of elements in a list.
    # We use a comprehension with "isinstance(v, (int, float))"
    # to prevent trying to sum non-numeric data, which would raise a TypeError.
    return sum(v for v in data.values() if isinstance(v, (int, float)))

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    expenses = {
        'rent': 1500,
        'food': 500,
        'gas': 50,
        'utilities': 300,
        'internet': 'Included in rent'
    }

    print(f"Total expenses: ${sumValues(expenses)}")
# EXERCISE
# Create a function that takes a list and creates a dictionary that groups the entries
# by the first letter.

def arrangeByLetter(lst: list) -> dict:
    # Initialize our resulting dictionary
    result = {}
    for entry in lst:
        # Use .setdefault to return an empty list ([]) if no entry exists, 
        # and append the entry either the existing list or the new empty list.
        result.setdefault(entry[0], []).append(entry)
    # Use a comprehension to sort each of the value lists. 
    result = {key: sorted(value) for key, value in result.items()}
    # Sort by key: convert into a list of key-value tuples, sort that list 
    # (which will be sorted by the first value, i.e. the key), then use the
    # dict() constructor function to convert back into a dictionary.
    return dict(sorted(result.items()))
    

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    fruits = ['apple', 'banana', 'cherry', 'cantalope', 'date', 'dragonfruit', 
              'avocado', 'grape', 'strawberry', 'mango', 'blackberry', 'grapefruit']
    print(arrangeByLetter(fruits))
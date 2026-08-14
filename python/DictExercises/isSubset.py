# EXERCISE
# Create a function to determine whether one dictionary is a subset of another,
# i.e. all the smaller one's key-pair pairs are in the other.

def isSubset(needle: dict, haystack: dict) -> bool:
     # .items() returns the key-value pairs of the dictionary expressed as tuples.
     # These can be operated on by the <= (subset) set operator.
     return needle.items() <= haystack.items()

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
     data1 = {'name': 'David', 'age': 39, 'city': 'Atlanta', 'state': 'GA'}
     data2 = {'name': 'David', 'city': 'Atlanta'}

     print(f"Is it a subset? {'Yes' if isSubset(data2, data1) else 'No'}.")
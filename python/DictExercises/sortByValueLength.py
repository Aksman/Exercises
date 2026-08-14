# EXERCISE
# Create a function that sorts a dictionary by the length of its (string) value.

def sortByValueLength(data: dict) -> dict:
    # This line does three things:
    # 1. The .items() method splits data into key-value pairs expressed as tuples.
    # 2. The key-value pairs are sorted. The key argument in sorted() takes a 
    # lambda function that return the length of the second item in the tuple, i.e. 
    # the value in the key-value pair.
    # 3. The sorted list of key-value tuples is converted back into a dictionary
    # using the dict() function.
    return dict(sorted(data.items(), key=lambda item: len(item[1])))

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    produce = {
        'a': 'apple',
        'b': 'banana',
        'c': 'cherries',
        'd': 'date',
        's': 'strawberry'
    }

    sortedProduce = sortByValueLength(produce)
    print(sortedProduce)

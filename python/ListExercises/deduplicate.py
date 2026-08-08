# EXERCISE
# Create a function that removes duplicates from a list.

# Method #1: Convert to set and back again.
def deduplicate1(elements: list) -> list:
    # This works because a Python set cannot accept duplicate values.
    # One big caveat: order is not preserved.
    return list(set(elements))

# Method #2: Use dict.fromkeys()
def deduplicate2(elements: list) -> list:
    # dict.fromkeys() creates a dictionary where the elements in the list
    # become the keys of the dict. Dictionary keys cannot be duplicated.
    # Converting back into a list takes all the keys.
    # This method preserves list order.
    return list(dict.fromkeys(elements))

# Method #3: Classic loop
def deduplicate3(elements: list) -> list:
    # Initialize the resulting list
    result = []
    # Create a dictionary that records what values we've found
    record = {}
    for el in elements:
        if el not in record:
            result.append(el)
            record[el] = True
    return result

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    import sys
    myList = sys.argv[1:] if len(sys.argv) > 1 else [8, 6, 7, 8, 5, 3, 6, 3, 0, 8, 9, 0, 8]
    print(f"Original: {myList}")
    print(f"Method #1: {deduplicate1(myList)}")
    print(f"Method #2: {deduplicate2(myList)}")
    print(f"Method #3: {deduplicate3(myList)}")

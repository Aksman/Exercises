# EXERCISE
# Create a function that splits a list into chunks of a specified size.

# Classic looping example
def chunk1(lst: list, size: int) -> list[list]:
    # Start by initializing our result.
    result = []
    for i in range(0, len(lst), size):
        # Note that in list slicing, Python gracefully adjusts an index out-of-bounds
        # to the nearest valid index, so there is no need for special handling for
        # the end of the list.
        result.append(lst[i:i + size])
    return result

# Using a list comprehension for tighter code
def chunk2(lst: list, size: int) -> list[list]:
    return [lst[i:i + size] for i in range(0, len(lst), size)]

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    import sys
    chunkSize = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    myList = sys.argv[2:] if len(sys.argv) > 2 else [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(chunk1(myList, chunkSize))
    print(chunk2(myList, chunkSize))
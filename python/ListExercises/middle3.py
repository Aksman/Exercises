# EXERCISE
# Create a function that returns the middle three elements in a list.

def middle3(lst: list) -> list:
    # Using floor division to make sure our middle Index is an integer
    midIndex = len(lst) // 2

    # This is to prevent out of range issues. A list with two elements
    # will simply return itself.
    start = max(midIndex - 1, 0)
    end = min(midIndex + 1, len(lst) - 1) + 1
    
    return lst[start:end]

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    import sys
    myList = sys.argv[1:] if len(sys.argv) > 1 else [1, 2, 3, 4, 5, 6, 7]
    sublist = middle3(myList)
    print(sublist)
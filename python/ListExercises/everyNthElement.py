# EXERCISE
# Create a function that returns part of the list that includes every nth element,
#  where the number n is specified.

def everyNthElement(elements: list, n: int) -> list:
    return elements[n - 1::n]

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    import sys
    n = sys.argv[1] if len(sys.argv) > 1 else 3
    myList = sys.argv[2:] if len(sys.argv) > 2 else ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    print(everyNthElement(myList, n))
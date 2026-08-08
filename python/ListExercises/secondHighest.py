# EXERCISE
# Return the second highest unique number from a list of numbers

def secondHighest(numbers: list[int|float]) -> int|float:
    # We convert to a set to get the unique numbers, then back to a list.
    uniques = list(set(numbers))

    # If we have only one unique value, return None.
    if len(uniques) < 2:
        return None

    # Sort the unique numbers in descending order.
    uniques.sort(reverse=True)

    # Return the second number in the sorted list
    return uniques[1]

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    import sys
    myList = [int(n) for n in sys.argv[1:]] if len(sys.argv) > 1 else [8, 6, 7, 5, 3, 0, 9, 8, 6, 7, 5, 3, 0, 9]
    print(f"Second highest: {secondHighest(myList)}")
# EXERCISE
# Create a functions that finds all subsets of a list.

def findAllSubsets(lst: list) -> list[list]:
    # Initialize with a empty list as the first outer list element.
    result = [[]]
    for el in lst:
        subsets = [subset + [el] for subset in result]
        result.extend(subsets)
    return result

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    import sys
    myList = sys.argv[1:] if len(sys.argv) > 1 else [1, 2, 3, 4, 5]
    allSubsets = findAllSubsets(myList)
    print(allSubsets)
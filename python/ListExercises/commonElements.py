# EXERCISE
# Create a function that takes an indetermate number of lists and returns
# a list of all elements they have in common.

def commonElements(*lsts: list) -> list:
    if len(lsts) == 0:
        return []
    if len(lsts) == 1:
        # If there is only one list, return every unique element
        return list(set(lsts[0]))

    # If there are two or more lists, begin with the first list
    result = set(lsts[0])

    # Apply the intersection of the result set and every subsequent list
    for lst in lsts[1:]:
        # "&" is the intersection operator for sets
        result = result & set(lst) 

    # Convert to a list and return
    return list(result)

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    lst2 = [8, 6, 7, 5, 3, 0, 9]
    lst3 = [0, 2, 0, 3, 0, 5, 0, 7]
    lst4 = [1, 1, 2, 3, 5, 8]

    print(f"Common elements: {commonElements(lst1, lst2, lst3, lst4)}")
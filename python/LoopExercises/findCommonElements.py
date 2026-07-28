# EXERCISE
# Find two elements in two lists

# Using the set() intersection method.

def findCommonElements1(list1: list, list2: list) -> list:
    # Convert to sets and use the intersection operator
    # Alternate syntax: return set(list1).intersection(set(list2))
    return list(set(list1) & set(list2))

# Use a loop

def findCommonElements2(list1: list, list2: list) -> list:
    common = []
    for el in list1:
        if el in list2:
            common.append(el)
    return common

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8, 9, 10]
    commonElements1 = findCommonElements1(list1, list2)
    print(f"Method #1: {commonElements1}")
    commonElements2 = findCommonElements2(list1, list2)
    print(f"Method #2: {commonElements2}")

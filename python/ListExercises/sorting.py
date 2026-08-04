# EXERCISE
# Sort a list
# Python already has two methods of basic sorting of a list: the .sort() method 
# and the sorted() function. The .sort() method sorts the original list. The sorted()
# function returns a sorted version of the list while leaving the original list unchanged.
# 
# Here I demonstrate one classic sorting algorithm: the quick sort, which uses a divide
# and conquer strategy. 

def manualSort(lst: list) -> list:
    # This algorithm is designed to use recursion. We need a point where we stop the resursion.
    # For a sorting algorithm that divides the list into sublists, that stopping point will be 
    # if we have a list of one element or less.
    if len(lst) <= 1:
        return lst

    # We need one element to use as a pivot point. For convenience, we'll use the first element.
    pivot = lst[0]

    # We divide the list into three sublists: everything less than, equal to, or greater than the pivot.
    # We initialize the sublists here.
    lowers = []
    equals = []
    uppers = []
    # Loop through the list and put each element in the sublist it belongs to.
    for el in lst:
        if el < pivot:
            lowers.append(el)
        elif el > pivot:
            uppers.append(el)
        else: # =
            equals.append(el)

    # The key here is that we recursively sort the less-than and greater-than lists. The equal-to list
    # does not need to be sorted. Each of the smaller lists will be sorted in the same manner, until 
    # we arrive at a place where all the sublists of sublists have one or zero elements, at which point
    # they will all be in order.
    return manualSort(lowers) + equals + manualSort(uppers)


# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    import sys
    import random
    myList = sys.argv[1:] if len(sys.argv) > 1 else random.choices(range(1, 101), k=15)

    print(f"Original: {myList}")
    # Demonstrating the sorted() function, which does not change the original list.
    print(f"Using sorted(): {sorted(myList)}")
    print(f"Original list unchanged: {myList}")

    # Demonstrating the manually coded sorting function above
    print(f"Using manualSort(): {manualSort(myList)}")
    print(f"Still unchanged: {myList}")

    # Demonstrating the .sort() method, which permanently changed the original list
    myList.sort()
    print(f"Now permanently sorted: {myList}")




# EXERCISE
# Perform several operations transforming a list.

def editingOperations(lst: list) -> tuple[list]:
    # Operation #1: Change the second element to 200
    lst[1] = 200
    lst1 = lst.copy()

    # Operation #2: Append 600 to the end of the list
    lst.append(600)
    lst2 = lst.copy()

    # Operation #3: Insert 300 at the third position
    lst.insert(2, 300)
    lst3 = lst.copy()

    # Operation #4: Remove the list element equal to 500 (by value)
    lst.remove(500)
    lst4 = lst.copy()

    # Operation #5: Remove the first element (remove by index)
    lst.pop(0)
    lst5 = lst.copy()

    # Return the saved lists representing the list in each state
    return lst1, lst2, lst3, lst4, lst5

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    import sys
    myList = sys.argv[1:] if len(sys.argv) > 1 else [100, 20, 400, 500]
    l1, l2, l3, l4, l5 = editingOperations(myList)
    print(f"Updated (Change): {l1}")
    print(f"Updated (Append): {l2}")
    print(f"Updated (Insert): {l3}")
    print(f"Updated (Remove 500): {l4}")
    print(f"Updated (Remove Index 0): {l5}")
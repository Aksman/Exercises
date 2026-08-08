# EXERCISE
# Create a function that lists all the items in one list that are not in the other.

def listDifference(origin: list, filter: list) -> list:
    # This is basically a set difference. Convert the lists into sets,
    # find the difference, and convert the result back into a list.
    return list(set(origin) - set(filter))

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    list1 = range(1, 11)
    list2 = [8, 6, 7, 5, 3, 0, 9]
    print(listDifference(list1, list2))
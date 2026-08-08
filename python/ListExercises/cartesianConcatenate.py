# EXERCISE
# Create a function that creates a new list that is a sort of cartesian product of two lists,
# where every item is an entry from one list concatenated with an entry from the other list.

def cartesianConcatenate(list1: list[str], list2: list[str] ) -> list[str]:
    # This can be accomplished very succintly using a list comprehension with two for clauses.
    # This works the same as two nested loops
    return [(a + ' ' + b) for a in list1 for b in list2]

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    list1 = ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'a', 'lazy', 'dog']
    list2 = ['every', 'good', 'boy', 'does', 'fine']

    product = cartesianConcatenate(list1, list2)
    for p in product:
        print(p)

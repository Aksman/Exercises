# EXERCISE
# Create a function that takes two lists and creates an interlaced list,
# using alternating elements from the two lists.

def interlace(list1: list, list2: list) -> list:
    # Initialize the combined list
    interlaced = []
    # Set the range to the maximum length of the two lists
    for i in range(0, max(len(list1), len(list2))):
        # Because idexes start at 0, we take even-indexed elements from the first list,
        # and odd-indexed elements from the second list.
        if i % 2 == 0:
            if i < len(list1):
                interlaced.append(list1[i])
            else: 
                # If we've run out of one list, we just finish with the other.
                interlaced.append(list2[i])
        else:
            if i < len(list2):
                interlaced.append(list2[i])
            else:
                # If we've run out of one list, we just finish with the other.
                interlaced.append(list1[i])

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    list1 = [1, 3, 5, 7, 9]
    list2 = [2, 4, 6, 8, 10]
    print(f"Interlaced List: {interlace(list1, list2)}")
# EXERCISE
# Given a list, return a list consisting of every other element.
# In this case, we will filter out the odd-number-indexed elements.

def filterEveryOther(listing: list) -> list:
    # Initialize the resulting list
    result = []
    # Use enumerate() in looping through the list so that we have
    # easy access for both the index and the value.
    for i, val in enumerate(listing):
        if i % 2 == 0:
            result.append(val)
    return result

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    import random
    listing = sys.argv[1:] if len(sys.argv) > 1 else random.choices(range(0, 101), k=10)
    print(f"List: {', '.join([str(item) for item in listing])}")
    print(f"Filtered: {', '.join(filterEveryOther([str(item) for item in listing]))}")
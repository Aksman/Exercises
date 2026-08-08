# EXERCISE
# Create a function that takes a list of strings and returns a list of those
# strings that are at least a specified length.

def filterByMinLength(texts: list[str], minLength: int) -> list[str]:
    # A list comprehension makes this very easy
    return [t for t in texts if len(t) >= minLength]

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    import sys
    minLength = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    myList = sys.argv[2:] if len(sys.argv) > 2 else ['Ohio', 'Indiana', 'Illinois', 'Wisconsin', 'Iowa']
    print(f"Filtered list: {filterByMinLength(myList, minLength)}")
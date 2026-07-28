# EXERCISE
# Create a function that returns the first non-repeating character in a string.

def firstNonRepeatingChar(text: str) -> str:
    # Initialize our dict where we will record character frequencies
    freq = {}

    # Loop through the characters in the string
    for c in text:

        # freq.get(c, 0) will return the value of freq[c] if it exists, or return the 
        # default value of 0. This line will initialize a new entry with a value of 1,
        # or increment it.
        freq[c] = freq.get(c, 0) + 1

    # Use list comprehension to return a list of all keys in freq where the value is 1.
    singles = [c for c in freq if freq[c] == 1]

    # Return the first entry in our list of singles
    return singles[0]

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    text = sys.argv[1] if len(sys.argv) > 1 else 'antidisestablishmentarianism'

    # Default: d
    print(firstNonRepeatingChar(text))
# EXERCISE
# Create a mixed string using alternating characters.
# Follow the following pattern: start with the first character of the first string, then the last character
# second string, then the second character of the first string followed by the second-to-last character
# of the second string and so forth.

def reverseInterlace(s1: str, s2: str) -> str:
    # Before we start, we will need the lengths of both string and the maximum length between the two.
    ln1 = len(s1)
    ln2 = len(s2)
    maxlength = max(ln1, ln2)

    # Initialize our result as an empty string.
    result = ''
    # Loop a number of times equal to the length of the longer string.
    for i in range(0, maxlength):
        # Until the end of the first string...
        if i < ln1:
            # Index 0 to ln1 - 1 (forward)
            result += s1[i]
        # Until the end of the second string...
        if i < ln2:
            # Index -1 to -ln2 (backward)
            result += s2[-1 - i]
    
    # Now that we're done, return the result
    return result

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    first = sys.argv[1] if len(sys.argv) > 1 else 'forward'
    second = sys.argv[2] if len(sys.argv) > 2 else 'backward'
    print(f"First: {first}")
    print(f"Second: {second}")
    print(f"Combined: {reverseInterlace(first, second)}")
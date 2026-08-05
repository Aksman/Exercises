# EXERCISE
# Create a function that finds the longest string in a list

# Method #1: Loop with tracking variable
def longestString1(texts: list[str]) -> str:
    longest = ''
    for t in texts:
        if len(t) > len(longest):
            longest = t
    return longest

# Method #2: Special case of max() function
def longestString2(texts: list[str]) -> str:
    # Setting the key argument to len makes max order to the strings
    # by length, not by alphabetical order
    return max(texts, key=len)

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    import sys
    myList = sys.argv[1:] if len(sys.argv) > 1 else ['apple', 'banana', 'cabbage', 'grape']

    print(f"Method #1: {longestString1(myList)}")
    print(f"Method #2: {longestString2(myList)}")
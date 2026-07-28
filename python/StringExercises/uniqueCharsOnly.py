# EXERCISE
# Create a function to determine if a string contains all unique characters.
# We'll create two functions, one using a more standard algorithm, and 
# one using a uniquely Pythonic method

def uniqueCharsOnly1(text: str) -> bool:
    # Set up a storage place to record which characters we've found.
    # We use a dict rather than a list because it is slightly faster
    # to look up a key in a dict than to look for a value in a list.
    found = {}
    # Loop through the string character by character
    for c in text:
        if c in found:
            # We've found a duplicate.
            return False
        else:
            found[c] = True
    # If we've reached this point, we've made it through without finding any duplicates.
    return True

def uniqueCharsOnly2(text: str) -> bool:
    # Convert the string to a set.
    # A set is an unordered collection type which can only contain unique values.
    textAsSet = set(text)

    # Return whether the length of the set is the same as the length of the string.
    # If the string contained all unique characters, this will be True.
    return len(textAsSet) == len(text)

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    text = sys.argv[1] if len(sys.argv) > 1 else 'python'
    print(f"{text}: {str(uniqueCharsOnly1(text))} or {str(uniqueCharsOnly2(text))}")

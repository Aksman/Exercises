# EXERCISE
# Remove duplicate characters from a string.
# This function preserves order, but takes out any character that has already appeared, 
# leaving only the first occurence.

def removeDuplicateChars(text: str) -> str:
    # Initialize the result string
    result = ''
    # Set up a record of which characters we've encountered.
    # We'll use a dict rather than a list, because it is faster to look up keys in
    # a dict that to search through a list.    
    found = {}

    for c in text:
        if c not in found:
            result += c
            # Record that we've found an instance of this character.
            found[c] = True
    
    return result

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    text = sys.argv[1] if len(sys.argv) > 1 else 'google'
    print(removeDuplicateChars(text))
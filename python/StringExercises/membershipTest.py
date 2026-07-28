# EXERCISE
# Create a membership test function involving two strings. Return true if every character in
# one string can be found in the other. Return false otherwise.
# This is an importance skill in data validation.

def membership(substring: str, mainstring: str, case_sensitive: bool = True) -> bool:

    #Convert strings to all lower case if we want our search to be case insensitive.
    if not case_sensitive:
        substring = substring.lower()
        mainstring = mainstring.lower()

    # Loop through all characters in substring
    for c in substring:

        # If not found, stop and return False
        if c not in mainstring:
            return False
        
    # If we made it this far, all characters were found, so return True
    return True

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    haystack = sys.argv[1] if len(sys.argv) > 1 else 'The quick brown fox jump over the lazy dog.'
    needles = sys.argv[2] if len(sys.argv) > 2 else 'rstlne'
    isMember = membership(needles, haystack)
    print(f"Search characters: {needles}")
    print(f"Search string: {haystack}")
    print(f"Membership test {'passed' if isMember else 'failed'}.")
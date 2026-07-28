# EXERCISE
# Create a function that rearranges that rearranges the characters in a string so that
# lower case letters are in the front, upper case letters are in the back, and
# everything else is filtered out.

def lowercaseFirst(text: str) -> str:
    # Initialize the first and last parts
    lowers = ''
    uppers = ''

    # Loop through the text to split up the letters.
    for c in text:
        if c.islower():
            lowers += c
        elif c.isupper():
            uppers += c

    # After we're done, put the two parts together and return the result
    return lowers + uppers

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    text = sys.argv[1] if len(sys.argv) > 1 else 'Hello World!'
    print(f"Original: {text}")
    print(f"Processed: {lowercaseFirst(text)}")
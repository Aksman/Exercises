# EXERCISE
# Write a function that toggles the case of all letters in a string.
# Uppercase becomes lowercase and vice versa.

# It would be simpler to use Python swapcase string method, 
# but we won't do that here.

def toggleCase(text: str) -> str:
    result = ''
    for c in text:
        if c.isupper():
            c = c.lower()
        elif c.islower():
            c = c.upper()
        result += c
    return result

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    text = sys.argv[1] if len(sys.argv) > 1 else 'Let\'s celebrate the 250th anniversary of the United States of America on July 4!'
    print(toggleCase(text))
    # For comparison sake
    print(text.swapcase())
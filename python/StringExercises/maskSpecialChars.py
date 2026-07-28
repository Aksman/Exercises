# EXERCISE
# Create a function to mask special characters (punctuation) in a string with a specified character.

import string

def maskSpecialChars(text: str, mask: str) -> str:
    masked = text
    for c in string.punctuation:
        masked = masked.replace(c, mask)
    return masked

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    text = sys.argv[1] if len(sys.argv) > 1 else "/*Jon is @developer & musician!!"
    print(maskSpecialChars(text, '#'))
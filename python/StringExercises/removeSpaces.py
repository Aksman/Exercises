# EXERCISE
# Remove all spaces from a string.
# This is different from the strip() method, which removes preceding and trailing whitespace.

def removeSpaces(text: str) -> str:
    return text.replace(' ', '')

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    text = sys.argv[1] if len(sys.argv) > 1 else ' P y t h o n '
    print(removeSpaces(text))
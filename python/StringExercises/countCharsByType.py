# EXERCISE
# Count the types of characters in a string: letters, digits, whitespace, and punctuation.

def countCharsByType(text: str) -> dict:
    counts = {
        'letters': 0,
        'digits': 0,
        'whitespace': 0,
        'punctuation': 0
    }

    for c in text:
        if c.isalpha():
            counts['letters'] += 1
        elif c.isdigit():
            counts['digits'] += 1
        elif c.isspace():
            counts['whitespace'] += 1
        else:
            counts['punctuation'] += 1

    return counts

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    text = sys.argv[1] if len(sys.argv) > 1 else 'Hello World!'
    print(f"Text: {text}")
    for key, value in countCharsByType(text).items():
        print(f"{key}: {value}")
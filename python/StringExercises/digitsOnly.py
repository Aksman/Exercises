# EXERCISE
# Create a function that returns only the digits in a string.

# This function makes use of a Python list comprehension.
# It creates a list of characters that are digits, then
# joins them together in a string.
def digitsOnly(text: str) -> str:
    return ''.join([c for c in text if c.isdigit()])

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    text = sys.argv[1] if len(sys.argv) > 1 else 'The price of 12 eggs is $3.99.'
    print(digitsOnly(text))
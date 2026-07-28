# EXERCISE
# Create a function to split a string into parts separated by a particular substring.
# This demonstrates the split() string method.

def tokenize(text: str, separator: str) -> list[str]:
    return text.split(separator)

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    text = sys.argv[1] if len(sys.argv) > 1 else 'Red|Orange|Yellow|Green|Blue|Indigo|Violet'
    sep = sys.argv[2] if len(sys.argv) > 2 else '|'
    parts = tokenize(text, sep)
    for part in parts:
        print(part)
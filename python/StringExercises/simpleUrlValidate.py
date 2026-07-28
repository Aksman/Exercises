# EXERCISE
# Perform a simplistic URL validation by checking if the string begins with 'https' and ends with '.com'
# This demonstrates the startsWith() and endsWith() string methods, which are more readable and less
# error prone than manual slicing for checking file formats or naming conventions.

def simpleUrlValidate(text: str) -> bool:
    if text.startswith('https') and text.endswith('.com'):
        return True
    return False

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    teststring = sys.argv[1] if len(sys.argv) > 1 else 'http://example.com'
    valid = simpleUrlValidate(teststring)
    print(f"\"{teststring}\" is {'' if valid else 'not '}a valid URL.")
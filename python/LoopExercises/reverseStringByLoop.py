# EXERCISE
# Reverse a string using a loop
# Normally in Python, we reverse a string using string slicing like this:
# myString[::-1]
# Here we will loop through the characters of the string in order to reverse it.

def reverseByLoop(text: str) -> str:
    result = ''
    for c in text:
        result = c + result
    return result

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    myText = sys.argv[1] if len(sys.argv) > 1 else 'Pythonic Loop'
    reverseText = reverseByLoop(myText)
    print(reverseText)
# EXERCISE
# Remove all punctuation and special characters from a string.

# This option uses a loop, which is easier to read for beginners.
def removeSpecialChars1(text: str) -> str:
    # Initialize as an empty string
    result = ''
    # Loop through characters in text
    for c in text:
        # Return if the character is alphanumeric or whitespace.
        if c.isalnum() or c.isspace():
            result += c
            
    return result

# This is an interesting Python-specific solution. 
# Use filter to filter out characters that are not alphanumeric or whitespace.
# Because filter() returns a filter object, we must use the join() method on an empty string
# to cast the result as a string.
def removeSpecialChars2(text: str) -> str:
    return ''.join(filter(lambda c: c.isalnum() or c.isspace(), text))

# Another Pythonic option is to use list comprehension
def removeSpecialChars3(text: str) -> str:
    return ''.join([c for c in text if c.isalnum() or c.isspace()])

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    text = sys.argv[1] if len(sys.argv) > 1 else "/*Jon is a\ndeveloper and @musician!!"
    print(removeSpecialChars1(text))
    print(removeSpecialChars2(text))
    print(removeSpecialChars3(text))
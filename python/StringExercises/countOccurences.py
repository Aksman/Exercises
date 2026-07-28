# EXERCISE
# Count the number of times that the substring occurs in the main string.
# Search should be case insensitive.
# This is a demonstration of searching text in a case insensitive manner
# as well as demonstration the count() string method.

def countOccurences(text: str, substring: str) -> int:
    return text.lower().count(substring.lower())

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    haystack = sys.argv[1] if len(sys.argv) > 1 else 'The mother and the father together smoothed the clothes.'
    needle = sys.argv[2] if len(sys.argv) > 2 else 'the'
    i = countOccurences(haystack, needle)
    print(f"There are {i} occurences of \"{needle}\" in the text.")
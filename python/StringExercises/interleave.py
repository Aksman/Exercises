# EXERCISE
# Create a function to interleave two string, where the resulting string alternates
# characters from the two strings.

def interleave(first: str, second: str) -> str:
    lenfirst = len(first)
    lensecond = len(second)
    maxlength = max(lenfirst, lensecond)
    
    result = ''
    # We number of times we loop through equals the length of the longer of the two strings.
    for i in range(0, maxlength):
        # Avoid trying to access out of ranges characters in our strings
        if i < lenfirst:
            result += first[i]
        if i < lensecond:
            result += second[i]

    return result

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    text1 = sys.argv[1] if len(sys.argv) > 1 else "abcdefg"
    text2 = sys.argv[2] if len(sys.argv) > 2 else "12345678"
    print(interleave(text1, text2))

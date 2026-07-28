# EXERCISE
# Check to see if given string is a rotation of another.
# I.e. 'ttlebo' is a rotation of 'bottle'.

# We could attempt to rotate the text to see if we can find a rotation the matches.
# However, here we will use a simple trick. We start by concatenating the first string 
# with itself. Then we will perform two checks: is the second string a substring of the
# double-first string, and are the two string equal length. If that's the case, then it's 
# a rotation.
def isTextRotation(text1: str, text2: str) -> bool:
    testString = text1 + text1
    return text2 in testString and len(text1) == len(text2)

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    text1 = sys.argv[1] if len(sys.argv) > 1 else 'bottle'
    text2 = sys.argv[2] if len(sys.argv) > 2 else 'ttlebo'
    if isTextRotation(text1, text2):
        print(f"\"{text2}\" is a rotation of \"{text1}\".")
    else:
        print(f"\"{text2}\" is not a rotation of \"{text1}\".")
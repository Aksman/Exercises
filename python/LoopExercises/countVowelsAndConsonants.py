# EXERCISE
# Create a function that counts both the vowels and consonants in a text string.

def countVowelsAndConsonants(text: str) -> dict[int]:
    # Initialize our return dict
    result = {'vowels': 0, 'consonants': 0}

    # We need a list of vowels to compare to.
    vowels = 'aeiou'

    # Set text to all lower case so we don't have to worry about case.
    for c in text.lower():

        # Ignore all characters that are not letters
        if c.isalpha():
            # Check if our character is in our list of vowels.
            if c in vowels:
                result['vowels'] += 1
            # If it's a letter and not a vowel, it's a consonant
            else:
                result['consonants'] += 1

    return result

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    text = sys.argv[1] if len(sys.argv) > 1 else "The quick brown fox jumps over the lazy dog."
    data = countVowelsAndConsonants(text)
    print(f"There are {data['vowels']} vowels and {data['consonants']} consonants.")
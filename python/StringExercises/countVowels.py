# EXERCISE
# Determine the number of vowels in a string.
# This exercise makes use of looping through characters in a string,
# plus the "in" operator.

def countVowels(text: str) -> str:
    # Initialize count to 0
    count = 0

    # Create a list of vowels to test against
    vowels = 'aeiouAEIOU'

    # Loop through characters in text
    for c in text:

        # If it matches one of the vowels, increment our count.
        if c in vowels:
            count += 1

    # Now that we're finished, return the count.
    return count


# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    text = sys.argv[1] if len(sys.argv) > 1 else 'Hello World!'
    numVowels = countVowels(text)
    print(f"Text: \"{text}\"")
    print(f"{numVowels} vowels found.")
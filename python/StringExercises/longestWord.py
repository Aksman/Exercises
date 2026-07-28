# EXERCISE
# Create a function that returns the longest word in a string.

# This would be the simplest, more traditional solution to the problem.
def longestWord1(text: str) -> str:
    # By default, the split() method separates on whitespace.
    words = text.split()

    # Cycle through the list of words to find the longest one.
    longest = words[0]
    for word in words[1:]:
        # Note that we only change the longest word if it is strictly longer.
        # So we will end up returning only the first word that is maximum length.
        if len(word) > len(longest):
            longest = word
    return longest

# A couple of differences here. One is how we split the text string, and the other
# is that we return a list with potentially more than one word at the maximum length.
import re

def longestWord2(text: str) -> list[str]:
    # Divide the text string by every group of non-alphanumeric characters.
    words = re.split(r'[^\w]+', text)

    # Initialize the list of longest words with the first word.
    longest = [words[0]]
    # Loop through all the remaining words.
    for word in words[1:]:
        # If the word is longer, reset the list.
        if len(word) > len(longest[0]):
            longest = [word]
        # If the word is the same length as the longest, add it to the list.
        elif len(word) == len(longest[0]):
            longest.append(word)
    
    return longest

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    text = sys.argv[1] if len(sys.argv) > 1 else 'The quick brown fox jumps over the lazy dog...'
    print(longestWord1(text))
    # Default: "dog..."

    print(longestWord2(text))
    # Default: ['quick', 'brown', 'jumps']
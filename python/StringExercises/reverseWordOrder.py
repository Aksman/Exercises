# EXERCISE
# Reverse the order of words in a string

import re

# This is the classic way to handle the problem. We split the string by whitespace
# (default for the split() method), reverse the order and rejoin.
def reverseWordOrderSimple(text: str) -> str:
    words = text.split()
    return ' '.join(words[::-1])

# This is a more complex and sophisticated solution to the problem. It reverses 
# word order while preserving all whitespace and punctuation.
def reverseWordOrder(text: str) -> str:
    # re.split() splits a string based on a separator defined by regex.
    # Here, we split by groupings of non-alphanumeric characters, i.e.
    # whitespace and punctuation. Encapsulating the regex in parentheses 
    # means we capture the separators, including them in our list. The result is
    # a list with alternating alphanumeric and non-alphanumeric substrings.
    # We use a list comprehension to filter out empty strings, because re.split()
    # will insert empty strings if the string begins or ends with a separator.
    wordsAndSpaces = [w for w in re.split(r'([^\w]+)', text) if w]
    
    # Create a list of of alphanumeric strings.
    words = [w for w in wordsAndSpaces if w.isalnum()]

    # We will want to cycle backward through the words list, so we start at index -1.
    wordIndex = -1
    
    # Initialize the result string.
    result = ''

    # Cycle through the full list of alternating alphanum and non-alphanum substrings.
    for ws in wordsAndSpaces:
        # If the word is alphanumeric, we replace it with a word from the words only 
        # list we made, which we are transversing backwards.
        if ws.isalnum():
            result += words[wordIndex]
            wordIndex -= 1
        # If the word is not alphanumeric, we attach it to the result unchanged.
        else:
            result += ws

    return result

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    text = sys.argv[1] if len(sys.argv) > 1 else "Python is fun!\nIt is truly a  remarkable language!"
    print(text)
    print(reverseWordOrderSimple(text))
    print(reverseWordOrder(text))
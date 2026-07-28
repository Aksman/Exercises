# EXERCISE
# Create a function to capitalize each word in a string

# The method we use here will require regex.
import re

def capitalizeWords(text: str) -> str:
    # Initialize our result as an empty string.
    result = ''

    # Split the string into alternating alphanumeric and non-alphanumeric(whitespace and punctuation)
    # substrings. We use the list comprehension to filter out any substrings that are empty (evaluate
    # to False), because if the beginning or end is not alphanumeric, then re.split() will insert an
    # empty string into the list.
    wordsAndSpaces = [w for w in re.split(r"([^\w]+)", text) if w]

    for word in wordsAndSpaces:

        # For every alphanumeric word, capitalize its first letter, then recombine it with the rest 
        # of the word. The first character is word[0], and word[1:] uses Python string slicing to 
        # start at the second character (index 1) and return everything from there to the end.
        if word.isalpha(): 
            word = word[0].upper() + word[1:]

        # All substrings, capitalize alphanumeric words and string of whitespace and punctuation, 
        # are added to the end of our result string.
        result += word
    
    return result


# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    text = sys.argv[1] if len(sys.argv) > 1 else 'hello world!   welcome to !python!'
    print(f"capitalizeWords(): {capitalizeWords(text)}")
    # A couple of similar Python string methods for comparison
    print(f".title(): {text.title()}")
    print(f".capitalize(): {text.capitalize()}")
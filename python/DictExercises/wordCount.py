# EXERCISE
# Create a function that creates a word count dictionary.

import re

def wordCount(text: str) -> dict[str, int]:
    wc = {}
    # We use re.split() rather than .split() in otder to handle both white space
    # and punctuation. The .split() string method splits by default by any group of whitespace
    # characters, but not by punctuation. re.split() using the regex pattern "\W+" will split
    # by any group of characters that are not "word characters", meaning letters, numeric digits, 
    # and the underscore ("_"). The "if word" portion of the list comprehension filters out any
    # empty strings, which you may have if the input string starts or ends with non-alphanumeric 
    # characters.
    words = [word.lower() for word in re.split(r'\W+', text) if word]
    for word in words:
        # As you can see, using the .get() method is cleaner than an if-else block. The .get()
        # dictionary method return the value of the specified key OR a default value if not found.
        # Here, we either add one to an already existing key, or create a new key and set its 
        # value to 1.
        wc[word] = wc.get(word, 0) + 1

    return wc

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    
    from pathlib import Path
    dir = Path(__file__).parent
    with(open(dir / 'post.txt', 'r', encoding='utf-8')) as file:
        content = file.read()

    wordTotals = wordCount(content)
    for word, count in wordTotals.items():
        print(f"{word}: {count}")
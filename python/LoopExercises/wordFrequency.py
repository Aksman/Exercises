# EXERCISE
# Count the occurences of each word in a text string.

import re

def wordFrequency(text: str) -> str:
    freq = {}
    words = [word for word in re.split(r'[^\w]+', text) if word]
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    text = sys.argv[1] if len(sys.argv) > 1 else 'How much wood would a woodchuck chuck if a woodchuck could chuck wood?'
    wordFreq = wordFrequency(text)
    title = 'Word Frequency'
    print(title)
    print('=' * len(title))
    for word, count in wordFreq.items():
        print(f"{word}: {count}")
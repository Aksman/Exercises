# EXERCISE
# Record the number of times a word appears in a text string.
import re

def wordFrequency(text: str) -> dict[int]:
    words = [w for w in re.split(r'[^\w]+', text.lower()) if w]

    freqs = {}
    for word in words:
        freqs[word] = freqs.get(word, 0) + 1

    return freqs

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    text = sys.argv[1] if len(sys.argv) > 1 else 'The cake was good, but the icing on the cake was even better.'
    for word, freq in wordFrequency(text).items():
        print(f"{word}: {freq}")
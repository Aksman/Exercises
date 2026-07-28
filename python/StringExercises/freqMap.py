# EXERCISE
# Create a frequency map for the characters in the string.
# I.e. create a dictionary that shows the number of time each character appears in the string.

def freqMap(text: str) -> dict:
    # Initialize the frequencies dict
    frequencies = {}

    # Loop through the text character by character
    for c in text:
        # The get method returns the value at the index specified, 
        # or substitutes a default value is it doesn't exist.
        frequencies[c] = frequencies.get(c, 0) + 1
        
    return frequencies

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    text = sys.argv[1] if len(sys.argv) > 1 else 'banananutmegpudding'
    freqs = freqMap(text)
    for k, v in freqs.items():
        print(f"{k}: {v}")
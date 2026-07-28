# EXERCISE
# Create a function to extract all alphanumeric words from a string, 
# i.e. words that contain both letters and digits.

def getAlphanumericWords(text: str) -> str:
    words = text.split() # Default is to split on whitespace, which is what we want
    # Initialize our list of alphanumeric words.
    alphanums = []
    for word in words:
        if any(c.isdigit() for c in word) and any(c.isalpha() for c in word):
            alphanums.append(word)

    return alphanums

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    text = sys.argv[1] if len(sys.argv) > 1 else 'David14 is SoftwareEngineer3 at Solutions Inc.'
    print(getAlphanumericWords(text))

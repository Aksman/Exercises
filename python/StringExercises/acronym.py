# EXERCISE
# Create a function that take a string and creates an acronym from the words.
import re

def acronym(text: str) -> str:
    # A list of exceptions for inclusion in the acronym
    WORD_EXCEPTIONS = [
        # Articles
        "a", "an", "the",
        
        # Coordinating Conjunctions
        "and", "but", "for", "nor", "or", "so", "yet",
        
        # Common Short Prepositions
        "at", "by", "in", "of", "on", "to", "up", "as", "with", "from"
    ]
    words = re.split(r'[^\w]+', text)

    acro = ''
    for word in words:
        if word.lower() not in WORD_EXCEPTIONS:
            acro += word[0].upper()

    return acro

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    text = ' '.join(sys.argv[1:]) if len(sys.argv) > 1 else 'light amplification by stimulated emission of radiation'
    print(acronym(text))
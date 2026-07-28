# EXERCISE
# Create a function that removes the nth character from a string.

def removeCharAtIndex(text: str, index: int) -> str:
    # We use string slicing to take the portions before and after the index, 
    # then recombine them. Remember that in slicing, the start parameter is
    # inclusive, but the stop parameter is exclusive.
    return text[:index] + text[index + 1:]

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    text = sys.argv[1] if len(sys.argv) > 1 else 'Tyrannosaurus'
    index = int(sys.argv[2]) if len(sys.argv) > 2 else 6
    # Expected output: Tyrannsaurus
    print(removeCharAtIndex(text, index))
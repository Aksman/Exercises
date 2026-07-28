# EXERCISE:
# Create a function that takes a single input string and returns the
# middle three characters as a single string.
# This exercise demonstrates calculating based on string length and 
# string slicing.

def middle3(text: str) -> str:
    # The "//" operator is floor division, returning the result if it 
    # is an integer, or returning the greatest integer less than it.
    middle = len(text) // 2

    # The string[x:y] construction is slicing, and works much the same way
    # as slicing iterable types like lists. The slicing is inclusive of the 
    # first index, but exclusive of the second, meaning you will have to 
    # increase last index by 1 if you want to include it.
    return text[middle - 1:middle + 2]

# Example usage.
# This block runs only if the script is run directly.
if __name__ == '__main__':
    import sys
    # Import the first command line argument after the script name.
    # If there is no such argument, substitute the default value.
    myText = sys.argv[1] if len(sys.argv) > 1 else 'ChuckAnyThing'
    # Expected default output: Any
    print(middle3(myText))
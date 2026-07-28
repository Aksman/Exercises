# EXERCISE
# Create a function that takes an input string and returns the 
# first, middle, and last character in the string.
# This exercise makes use of string indexing, plus calculating 
# based on string length.

def firstMiddleLast(text: str) -> str:
    # "//" is a floor division operator. It returns the result 
    # if it is an integer, or the greatest integer less than it.
    middle = len(text) // 2 
                            
    # The "+" operator is used to concatenate strings.
    # Individual characters can be accessed with indexes much 
    # like iterable types like lists and tuples. 
    # text[0] is the first character in the string.
    # Characters can be indexed backward from the end using 
    # negative numbers.
    return text[0] + text[middle] + text[-1]

# Example usage.
# This block only executes if the script is run directly.
if __name__ == '__main__':
    import sys

    # This retrieves the first command line argument after the script name.
    # If there is no argument, we substitute the default 'David'.
    myText = sys.argv[1] if len(sys.argv) > 1 else 'David'
    # Expected default output: Dvd
    print(firstMiddleLast(myText))

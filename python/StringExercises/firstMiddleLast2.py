# EXERCISE
# Given any number of strings, create a string using the 
# first, middle, and last characters of each of them.
# This function will demonstrate complex concatenation,
# calculating based on string length, and an indetermate 
# number of arguments.

# The *args construction allows a function with a indeterminate
# number of arguments. The arguments are imported into the function
# as a tuple.
def firstMiddleLast2(*args: str) -> str:
    # Initialize the beginning, middle, and end of our returned string.
    start, middle, end = '', '', ''

    # We iterate over the args tuple.
    for text in args:
        # The "//" operator is floor division, returning the result if it 
        # is an integer, or returning the greatest integer less than it.
        middleIndex = len(text) // 2

        # Concatenate the first, middle, and last characters to the 
        # start, middle, and end partitions we are building.
        start += text[0]
        middle += text[middleIndex]
        end += text[-1]

    # Combined the three parts and return
    return start + middle + end

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    gestalt1 = firstMiddleLast2('Alvin', 'Simon', 'Theodore')
    print(gestalt1)
    gestalt2 = firstMiddleLast2('Keith', 'Lance', 'Pidge', 'Allura', 'Hunk')
    print(gestalt2)

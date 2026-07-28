# EXERCISE
# Create a function that removes all the empty strings and Nones from a list of strings.

def removeEmpty(strings: list[str]) -> list[str]:
    # The filter function filters a list based on the function in the first argument.
    # If None is passed as the first argument, then all elements that are "falsy" are 
    # removed, like False, the number 0, None, or an empty string.
    return list(filter(None, strings))

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    strings = list(sys.argv[1:]) if len(sys.argv) > 1 else ['one', 'two', '', 'three', None, 'four']
    nonempty = removeEmpty(strings)
    print(nonempty)
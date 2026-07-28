# EXERCISE
# Create a function that inserts a piece of text into the middle of a string.
# This function will demonstrate calculation based on the length of the string,
# plus spliting and concatenating strings.

def insertText(container: str, insert: str) -> str:
    # The "//" operator is floor division, returning the result if it 
    # is an integer, or returning the greatest integer less than it.
    middle = len(container) // 2

    # In Python's slice notation, string[:index] is the substring that starts at
    # the beginning and goes to index. string[index:] goes from index to the end.
    return container[:middle] + insert + container[middle:]

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    container = sys.argv[1] if len(sys.argv) > 1 else 'haystack'
    insert = sys.argv[2] if len(sys.argv) > 2 else 'needle'
    # Default output should be: haysneedletack
    print(insertText(container, insert))
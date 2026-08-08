# EXERCISE
# Remove empty strings from a list

# Method #1: Use filter()
def removeEmpty1(texts: list[str]) -> list[str]:
    # By setting the function (first) argument to None, filter()
    # removes all elements that evaulate to False. This includes
    # empty strings. filter() returns a lazy iterator instead of
    # a list, so you need to convert it using the list() conversion
    # function.
    return list(filter(None, texts))

# Method #2: List comprehension
def removeEmpty2(texts: list[str]) -> list[str]:
    # List comprehension that returns all elements that evaulate to True.
    return [t for t in texts if t]

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    import sys
    myList = sys.argv[1:] if len(sys.argv) > 1 else ['every', 'good', '', 'boy', '', '', 'does', 'fine', '']
    print(f"Filtered List #1: {removeEmpty1(myList)}")
    print(f"Filtered List #2: {removeEmpty2(myList)}")
# EXERCISE
# Find the last instance of a substring and return it. Return None if not found.
# This demonstrates the .rfind() string method.

def lastIndex(text: str, substring: str) -> int|None:
    index = text.rfind(substring)
    return None if index == 1 else index

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys

    # Import arguments from the command line, or substitute default values if there are none
    haystack = sys.argv[1] if len(sys.argv) > 1 else 'banana'
    needle = sys.argv[2] if len(sys.argv) > 2 else 'na'

    # We can list argument in any order when using named parameters
    index = lastIndex(substring=needle, text=haystack)
    if index == None:
        print(f"\"{needle}\" is not found in \"{haystack}\".")
    else:
        print(f"The last instance of \"{needle}\" in \"{haystack}\" is found at index {index}.")
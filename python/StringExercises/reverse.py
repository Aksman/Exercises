# EXERCISE
# Create a function that reverses a string
# This exercise demonstrates the use of the step parameter in string slicing

def reverse(text: str) -> str:
    # The third parameter in string slicing is the step parameter.
    # It specifies how the slice moves between characters. Default is 1, 
    # meaning go forward one character at a time. Here we go backward 1 character 
    # at a time. Using the default start and stop parameters means we use the 
    # whole string. The result will be the string in reverse.
    return text[::-1]

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    text = sys.argv[1] if len(sys.argv) > 1 else 'Reverse me'
    print(reverse(text))
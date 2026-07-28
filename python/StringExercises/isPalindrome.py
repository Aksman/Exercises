# EXERCISE
# A classic programming exercise! Create a function that determines if a string is a palindrome.
# For this exercise, we will ignore case, whitespace, and puncuation, which paradoxically means 
# we have to account for all three in our function.

def isPalindrome(text: str) -> bool:
    # Create a list of all alphanumeric characters using Python list comprehension.
    # Join that list back together in a string, then set to all lower case.
    filtered = ''.join([c for c in text if c.isalnum()]).lower()

    # Return True or False whether the filtered string is the same forward and backward.
    # We use Python string slicing using the default start and stop values at the beginning
    # and end of the string and a step value of -1 indicating that we step backward one character
    # at a time.
    return filtered == filtered[::-1]

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    text = sys.argv[1] if len(sys.argv) > 1 else 'A man, a plan, a canal Panama'
    decision = isPalindrome(text)
    print(f"The text \"{text}\" is {'' if decision else 'not '}a palindrome.")
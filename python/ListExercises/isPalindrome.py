# EXERCISE
# Create a function to determine if a list is a palindrome.

def isPalindromeList(lst: list) -> bool:
    # List slicing works the same as string slicing.
    return lst == lst[::-1]

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    import sys
    myList = sys.argv[1:] if len(sys.argv) > 1 else [1, 2, 3, 4, 3, 2, 1]
    print(f"Original List: {myList}")
    print(f"Is it a palindrome? {'Yes' if isPalindromeList(myList) else 'No'}.")

    

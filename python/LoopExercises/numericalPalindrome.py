# EXERCISE
# Determine if an integer is a palindrome

def numberIsPalindrome(num: int) -> bool:
    copy = num
    reversal = 0
    while copy > 0:
        rem = copy % 10
        copy //= 10
        reversal = 10 * reversal + rem
    return num == reversal

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    num = int(sys.argv[1]) if len(sys.argv) > 1 else 8675309
    choice = numberIsPalindrome(num)
    print(f"The number {num} is {'not ' if not choice else ''}a palindrome.")

        
# EXERCISE
# Reverse the order of digits in an integer

# The easy way: Convert to a string and reverse the order
def reverseInt1(num: int) -> int:
    # Convert to string, reverse the order, then convert back to int
    return int(str(num)[::-1])

def reverseInt2(num: int) -> int:
    result = 0
    while num > 0:
        rem = num % 10
        num = num // 10
        result = 10 * result + rem
    return result

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    num = sys.argv[1] if len(sys.argv) > 1 else 8675309
    print(f"Method #1: {reverseInt1(num)}")
    print(f"Method #2: {reverseInt2(num)}")
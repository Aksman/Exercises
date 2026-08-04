# EXERCISE
# Create a function that calculates a triangular number using a recursive function.
# A triangular number is a number that results when the natural numbers are added together.
# I.e. 1, 3 (1 + 2), 6 (1 + 2 + 3), and so on.

def triangularNum(n: int):
    # n must be a natural number.
    if n <= 0:
        raise ValueError('Number must be at least 1.')
    # Handling our ending call.
    if n == 1:
        return 1
    else:
        # Our recursive call.
        return n + triangularNum(n - 1)

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    import sys
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    print(triangularNum(n))
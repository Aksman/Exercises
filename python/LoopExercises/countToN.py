# EXERCISE
# Create a function to print the first N natural numbers.

def countToN(n: int):
    # For range, the start parameter is inclusive, but the end paramater is exclusive.
    # In order to stop at n, we need an end parameter of n + 1.
    for i in range(1, n + 1):
        print(i)

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    countToN(n)
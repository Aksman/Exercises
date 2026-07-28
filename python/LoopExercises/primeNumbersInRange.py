# EXERCISES
# Create a function that returns all prime numbers within a range.

import math

def primesInRange(start: int, end: int) -> list[int]:
    # Find all the prime numbers less than or equal to end.
    # Initialize a list where all indexed elements being set to True
    primes = [True] * (end + 1)
    # 0 and 1 are not prime numbers
    primes[0] = False
    primes[1] = False

    # Because we are knocking out all the multiples of the primes we find,
    # we only need to check numbers less than the square root of end.
    for i in range(2, math.floor(math.sqrt(end))):
        # If the number hasn't already been set to False, it's prime.
        if primes[i]:
            # Now set all the multiples of i to False, except i itself.
            j = 2
            while i * j <= end:
                primes[i * j] = False
                j += 1

    # Return all the indexes that are still set to True within our range.
    return [index for index, val in enumerate(primes) if val and start <= index <= end]

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    start = sys.argv[1] if len(sys.argv) > 1 else 51
    end = sys.argv[2] if len(sys.argv) > 2 else 100
    primes = primesInRange(start, end)
    for p in primes:
        print(f"{p} ", end='')
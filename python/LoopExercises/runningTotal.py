# EXERCISE
# Given a list of integers, create a new list representing the cumulative sums.

def cumulativeSums(numbers: list[int]) -> list[int]:
    runningTotal = 0
    result = []
    for n in numbers:
        runningTotal += n
        result.append(runningTotal)
    return result

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    numbers = [int(n) for n in sys.argv[1:]] if len(sys.argv) > 1 else [1, 2, 3, 4]
    print(cumulativeSums(numbers))
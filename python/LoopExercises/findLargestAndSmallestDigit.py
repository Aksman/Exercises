# EXERCISE
# Find the largest and smallest digit in an integer

def findLargestAndSmallestDigit1(num: int) -> tuple[int]:
    largest = 0
    smallest = 9

    numStr = str(num)
    for d in numStr:
        dInt = int(d)
        if dInt < smallest:
            smallest = dInt
        if dInt > largest:
            largest = dInt

    return largest, smallest

def findLargestAndSmallestDigit2(num: int) -> tuple[int]:
    largest = 0
    smallest = 9

    while num > 0:
        rem = num % 10
        num //= 10
        if rem < smallest:
            smallest = rem
        if rem > largest:
            largest = rem
    return largest, smallest

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    num = int(sys.argv[1]) if len(sys.argv) > 1 else 86753

    largest, smallest = findLargestAndSmallestDigit1(num)
    print(f"Method #1: smallest: {smallest}, largest: {largest}")

    largest, smallest = findLargestAndSmallestDigit2(num)
    print(f"Method #2: smallest: {smallest}, largest: {largest}")

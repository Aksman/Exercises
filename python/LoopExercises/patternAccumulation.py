# EXERCISE
# Create a function that records the sum of numbers that are in the following pattern:
# 2 + 22 + 222 + 2222 + 22222 + ...

def patternAccumulation(limit: int) -> int:
    currentAddend = 0
    runningTotal = 0
    for i in range (0, limit):
        currentAddend = currentAddend * 10 + 2
        runningTotal += currentAddend
    return runningTotal

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    limit = sys.argv[1] if len(sys.argv) > 1 else 5
    myNum = patternAccumulation(limit)
    print(myNum)
# EXERCISE
# Create a function that iterates through and prints a list of numbers.
# Implement the following conditions:
# 1. If the number is divisible by 5, skip it.
# 2. If the number is divisible by 25, stop printing and exit.
# 3. Otherwise, print the number.
# This exercise demonstrates the use of break and continue in a loop.
import time

def flowControl1(numList: list[int]):
    for num in numList:
        if num % 25 == 0:
            break
        elif num % 5 == 0:
            continue
        else:
            print(num)
            time.sleep(0.5)

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    import random
    nums = [int(arg) for arg in sys.argv[1:]] if len(sys.argv) > 1 else random.choices(range(1,501), k=500)
    flowControl1(nums)
    print("\n\n")
    time.sleep(2)
    print(nums)
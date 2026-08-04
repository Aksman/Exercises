# EXERCISE
# Create a function that takes any number of numerical arguments and returns a list 
# of progressive sums.
# This is a demonstration of a variable length argument list.

def progressiveSum(*addends: int|float) -> list[int|float]:
    sums = []
    for addend in addends:
        if len(sums) == 0:
            sums.append(addend)
        else:
            sums.append(addend + sums[-1])
    return sums

# Example usage
# This block runs only when this script is accessed directly (i.e. not imported).
if __name__ == '__main__':
    # Confirm it works for a long list of numerical arguments
    listOfSums1 = progressiveSum(14, 17, 11, 22, 8, 3, 18)
    print(listOfSums1)

    # Confirm it works for a single argument
    listOfSums2 = progressiveSum(42)
    print(listOfSums2)

    # Confirm it works with floating point arguments
    listOfSums3 = progressiveSum(7.14, 3.32, 1.21, 8, 5.5)
    print(listOfSums3)
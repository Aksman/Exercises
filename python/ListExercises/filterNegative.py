# EXERCISE
# Filter the negative numbers from a list of numbers.
# Perform the operation on the original list, without creating a copy.

# This is a particular challenge, because if as you iterate through the list,
# if you find a negative numbers at index n, after removing it, the number at 
# index n + 1 becomes the value at index n. If you are using a standard for loop, 
# you'll end up skipping over the value that was at the n + 1 position.
 
def filterNegative1(numbers: list[int|float]):
    # Easiest method: iterate backwards through the list indices
    for i in range(len(numbers) - 1, -1, -1):
        if numbers[i] < 0:
            del numbers[i]

def filterNegative2(numbers: list[int|float]):
    # Harder method, conditional iteration
    i = 0
    while i < len(numbers):
        if numbers[i] < 0:
            del numbers[i]
        else:
            i += 1

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    def convertNumber(text: str) -> int|float:
        try:
            return int(text)
        except ValueError:
            try:
                return float(text)
            except ValueError:
                raise ValueError('A numerical string is required.')
    import sys
    myList = [convertNumber(n) for n in sys.argv[1:]] if len(sys.argv) > 1 else [8, 6, -7, -5, 3, 0, 9]
    myList2 = myList.copy()

    print(f"The list: {myList}")
    filterNegative1(myList)
    print(f"Method #1: {myList}")
    filterNegative2(myList2)
    print(f"Method #2: {myList2}")
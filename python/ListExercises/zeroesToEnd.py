# EXERCISE
# Create a function that moves all the zeroes in a list of numbers to the end of the list.

def zeroesToEnd1(numbers: list[int|float]) -> list[int|float]:
    # Simplest solution: Create two list comprehensions to filter all zeroes and non-zeroes
    # into their own lists, then recombined.
    zeroes = [n for n in numbers if n == 0]
    nonzeroes = [n for n in numbers if n != 0]

    return nonzeroes + zeroes

def zeroesToEnd2(numbers: list[int|float]) -> list[int|float]:
    # Harder solution: Move in place
    i = 0
    # A temporary separate list to store the zeroes is necessary. Otherwise, it would go into 
    # an infinite loop at the end.
    zeroes = []
    # Note that this will stop at the end even when the list shortens.
    while i < len(numbers):
        if numbers[i] == 0:
            z = numbers.pop(i)
            zeroes.append(z)
        else:
            # Keep the pointer in place if we moved the zero,
            # otherwise move to the next index.
            i += 1
    return numbers + zeroes

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    def convertNumber(text: str) -> int|float:
        try:
            return int(text)
        except:
            try: 
                return float(text)
            except:
                raise ValueError('Invalid non-numerical string.')

    import sys
    myList = [convertNumber(n) for n in sys.argv[1:]] if len(sys.argv) > 1 else [1, 8, 0, 0, 8, 6, 7, 5, 3, 0, 9]
    print(f"Original List: {myList}")
    print(f"Method #1: {zeroesToEnd1(myList)}")
    print(f"Method #2: {zeroesToEnd2(myList)}")
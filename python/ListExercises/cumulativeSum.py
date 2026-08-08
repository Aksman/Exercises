# EXERCISE
# Create a function that turns a list of numbers into a list of cumulative sums.

def cumulativeSums(numbers: list[int|float]) -> list[int|float]:
    c = 0
    result = []
    for n in numbers:
        c += n
        result.append(c)
    return c

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
                raise ValueError('String cannot be converted to a number.')
            
    import sys
    myList = [convertNumber(n) for n in sys.argv[1:]] if len(sys.argv) > 1 else [1, 2, 3, 4, 5]
    print(cumulativeSums(myList))
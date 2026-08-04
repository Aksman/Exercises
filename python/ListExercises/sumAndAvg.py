# EXERCISE
# Create a function that returns both the sum and average of a list of numbers
#

def sumAndAvg(numbers: list[int|float]) -> tuple[int|float]:
    mySum = sum(numbers)

    myAvg = mySum / len(numbers)

    return mySum, myAvg

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
                raise ValueError(f"Invalid numeric string \"{text}\"")
            
    import sys
    myList = [convertNumber(t) for t in sys.argv[1:]] if len(sys.argv) > 1 else [1, 2, 3, 4, 5]
    s, avg = sumAndAvg(myList)
    print(f"Sum: {s}")
    print(f"Average: {avg}")
    
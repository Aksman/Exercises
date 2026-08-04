# EXERCISE
# Create a function that returns both the minimum and maximum in a list of numbers.


def minAndMax(numbers: list[int|float]) -> tuple[int|float]:
    # No need to re-invent the wheel. Python already provides min() and max() functions.
    return min(numbers), max(numbers)

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
    myNumbers = [convertNumber(n) for n in sys.argv[1:]] if len(sys.argv) > 1 else [91, 24, 63, 7, 85, 50]
    lowest, highest = minAndMax(myNumbers)
    print(f"Min: {lowest}, Max: {highest}")
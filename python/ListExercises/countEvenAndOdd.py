# EXERCISE
# Given a list of integers, count the number of even and odd numbers.

def evenAndOdd(numbers: list[int]) -> tuple[int]:
    evens = 0
    odds = 0
    for n in numbers:
        if n % 2 == 0:
            evens += 1
        else:
            odds += 1
    return evens, odds

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
    import random
    myNumbers = [convertNumber(n) for n in sys.argv[1:]] if len(sys.argv) > 1 else random.choices(range(1, 101), k=10)
    print(myNumbers)
    evens, odds = evenAndOdd(myNumbers)
    print(f"Even: {evens}")
    print(f"Odd: {odds}")
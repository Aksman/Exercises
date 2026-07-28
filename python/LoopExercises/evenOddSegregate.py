# EXERCISE
# Create a function that takes a list of integers and reorganizes them so that
# even numbers are in the front and odd numbers are in the back.

def evenOddSegregate(numbers: list[int]) -> list[int]:
    # Initialize our lists of evens and odds
    evens = []
    odds = []

    # Loop through the list
    for n in numbers:
        if n % 2 == 0: # Even
            evens.append(n)
        else: # Odd
            odds.append(n)
            
    # Combine the two lists and return
    return evens + odds


# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    myList = [int(n) for n in sys.argv[1:]] if len(sys.argv) > 1 else range(1, 11)
    reordered = evenOddSegregate(myList)
    print(reordered)


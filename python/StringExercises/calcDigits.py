# EXERCISE
# Create a function to make calculations based on the digits in a string, and only the digits.

def calcDigits(text: str, calc: str|list[str]) -> dict[int|float|list[int|float]]:
    if type(calc) == 'str':
        calc = [calc]

    # Initialize our list of digits
    digits = []
    for c in text:
        if c.isdigit():
            digits.append(int(c))

    # Initialize our results dict
    results = {}
    # Make the specifed calculations. Options are sum, average, median, mode, min, and max.
    for calcType in calc:
        # The sum of all the digits
        if calcType == 'sum':
            results['sum'] = sum(digits)
        # The average (mean) of all the digits
        elif calcType == 'average':
            results['average'] = sum(digits) / len(digits)
        # The median, i.e. the number in the middle of all the numbers if sorted in order.
        elif calcType == 'median':
            sortedDigits = sorted(digits)
            numDigits = len(sortedDigits)
            middle = numDigits // 2
            # If there are an odd number of digits, then middle with be exactly in the middle.
            # If there are an even number of digits, the middle will be between two numbers, and
            # we will need to take the average between them.
            if numDigits % 2 == 0:
                results['median'] = (sortedDigits[middle - 1] + sortedDigits[middle]) / 2
            else:
                results['median'] = sortedDigits[middle]
        # The number that occurs the most in the list. There can be more than one number,
        # so we return a list for this one.
        elif calcType == 'mode':
            counts = {}
            for i in digits:
                counts[i] = counts.get(i, 0) + 1
            maxCount = max(counts.values())
            results['mode'] = [num for num, count in counts.items() if count == maxCount]
        # The lowest number found
        elif calcType == 'min':
            results['min'] = min(digits)
        # The highest number found
        elif calcType == 'max':
            results['max'] = max(digits)
    return results

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    text = sys.argv[1] if len(sys.argv) > 1 else """Hi, Sarah. The 54th birthday party for Tamara 
    will be held at the 4 Seasons Hotel on July 26. The party starts at 6:00, but you will need 
    to be there at 5 to help set up. We will need to be conclude by 9 pm. The hotel is at 835 7th Street, 
    Alpharetta, GA 30005. If you have any questions, call or text me at 309-555-2818, or email me
    at john.smith1477@example.com."""
    calcs = ['sum', 'average', 'median', 'mode', 'min', 'max']
    data = calcDigits(text, calcs)
    for key, value in data.items():
        print(f"{key}: {value}")

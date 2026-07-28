# EXERCISE
# Create a function to determine if an integer is a perfect number.
# An integer is a perfect number if it is equal to the sum of all its
# whole number factors excluding itself.

def isPerfectNumber(num: int) -> bool:
    if num < 0:
        raise ValueError('A negative number cannot be a perfect number.')
    if num == 1:
        return False
    # Initialize two sets of factors.
    lowerFactors = [1]
    upperFactors = []

    # There can be no factors greater than num/2, so we start by only checking 
    # those numbers. Over the course of our search we will likely be defining this
    # upperLimit downward.
    upperLimit = num // 2
    i = 2
    while i < upperLimit:
        if num % i == 0:
            # Add to lowerFactors
            lowerFactors.append(i)
            # If i is a factor, num / i must also be a factor.
            # Also revise upperLimit downward to num / i.
            upperLimit = int(num / i)
            # Prevent double recording in case num is a prefect square.
            if i != num / i:
                upperFactors.append(upperLimit)
        i += 1

    # If the sum of all factors equals our number, return True. Else return False.
    if sum(lowerFactors) + sum(upperFactors) == num:
        return True
    return False
            
# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 28
    assess = isPerfectNumber(n)
    print(f"{n} is {'' if assess else 'not '}a perfect number.")
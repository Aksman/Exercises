# EXERCISE
# Create a function that takes a list of numbers and prints out a progressive sum, 
# where each number takes the given number and adds it to all previous numbers.
# The function then prints out the resulting list of numbers.
# This demonstrates a variable length argument list as well as a function that contains
# internal functions.

def printProgressiveSums(length: int):

    # This internal function converts a numeric string to either an int or a float,
    # depending on what is entered.
    def toNumber(numeric: str) -> int|float:
        try:
            return int(numeric)
        except ValueError:
            try:
                return float(numeric)
            except:
                raise ValueError('String cannot be converted to int or float.')

    sums = []
    while len(sums) < length:
        try:
            # Note the use of the internal function here.
            nextNum = toNumber(input('Enter the next number: '))
            if len(sums) == 0:
                sums.append(nextNum)
            else:
                sums.append(nextNum + sums[-1])
        except:
            print('Invalid number.')

    for s in sums:
        print(f"{s} ", end='')

# Example usage:
# The following block will only run when this script is run directly (i.e. not imported)
if __name__ == '__main__':
    printProgressiveSums(5)

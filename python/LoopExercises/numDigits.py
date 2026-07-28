# EXERCISE
# Count the number of digits in an integer

# The easy way: convert the integer to a string and return the length.
def countDigits1(num: int) -> int:
    return  len(str(num))

def countDigits2(num: int) -> int:
    numDigits = 0
    while num > 0:
        num //= 10
        numDigits += 1
    return numDigits

def countDigits3(num: int) -> int:
    power = 1
    while 10 ** power <= num:
        power += 1
    return power

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    num = int(sys.argv[1]) if len(sys.argv) > 1 else 8675309
    print(num)
    print(f"Method #1: {countDigits1(num)}")
    print(f"Method #2: {countDigits2(num)}")
    print(f"Method #3: {countDigits3(num)}")
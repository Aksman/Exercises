# EXERCISE
# Demonstrate different methods of converting an integer to binary format.

def demoConvertToBinary(num: int):

    # Method #1a: Use the bin() function
    print('Method #1a:', bin(num))

    # The bin() function adds a '0b' prefix to the number. You 
    # can get rid of it with slicing.
    print('Method #1b:', bin(num)[2:])

    # The f-string method
    print(f"Method #2a: {num:b}")

    # Alternately, the string format method.
    print('Method #2b:', "{:b}".format(num))

    # Or use the format() function
    print('Method #3:', format(num, 'b'))

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    num = int(sys.argv[1]) if len(sys.argv) > 1 else 23
    demoConvertToBinary(num)
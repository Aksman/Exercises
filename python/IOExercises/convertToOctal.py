# EXERCISE
# A demonstration of different methods of converting to an octal number.

def demoConvertToOctal(num: int):
    # Method #1: Use '%o' to format it as an octal number.
    print('Method #1:', '%o' % num)

    # Method #2: Use the built-in oct() function. Note that this will produce
    # a string with the '0o' prefix.
    print('Method #2:', oct(num))

    # Method #3: Format a string using the ":o" specifier.
    print('Method #3a:', f"{num:o}")
    print('Method #3b:', "{:o}".format(num))

    # Method #4: Use the format() function.
    print('Method #4:', format(num, 'o'))

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    num = int(sys.argv[1]) if len(sys.argv) > 1 else 16
    demoConvertToOctal(num)
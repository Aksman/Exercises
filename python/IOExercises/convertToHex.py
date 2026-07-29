# EXERCISE
# Demostrate converting an int to hexidecimal.

def demoConvertToHex(num: int):
    # Method #1a: hex() function
    print(f"Method #1a: {hex(num)}")

    # Removing the "0x" prefix from the above.
    print(f"Method #1b: {hex(num)[2:]}")

    # Method #2: f-strings
    print(f"Method #2a: {num:x}")
    print(f"Method #2b: {num:X}") # upper case letters

    # Method #3: .format() method
    print("Method #3a:", "{:x}".format(num))
    print("Method #3b:", "{:X}".format(num))

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    num = int(sys.argv[1]) if len(sys.argv) > 1 else 255
    demoConvertToHex(num)

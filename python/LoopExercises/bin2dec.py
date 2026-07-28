# EXERCISE
# Create a function that converts a binary string into a decimal integer.
# Perform the conversion by looping, not using int(binaryString, 2).

def bin2dec(binaryString: str) -> int:
    # If we revese the string, the character index will line up perfectly 
    # with the powers represented.
    reverseBinary = binaryString[::-1]

    # Initialze our number
    dec = 0

    # Use the enumerate() function to cycle through the string's characters,
    # keeping track of both the index and the character value.
    for index, char in enumerate(reverseBinary):
        if char not in ['0', '1']:
            raise ValueError('Not a binary string.')
        dec += int(char) * 2 ** index

    return dec

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    binary = sys.argv[1] if len(sys.argv) > 1 else '11001001'
    print(bin2dec(binary))

# EXERCISE
# Demostrate using the split() method to divide a single input into multiple entries.

def demoSplitInput():
    # We initialize the names list, then loop the input until the user actually gives us
    # three names.
    names = []
    while len(names) == 0:
        singleInput = input('Give me three names separated by spaces: ')

        # By default, the .split() method splits on any group of consecutive whitespace characters.
        inputs = singleInput.split()
        if len(inputs) < 3:
            print(f"I need at least three names. You only gave me {len(inputs)}.")
        else:
            names = inputs

    print('Your names:')
    for name in names:
        print(name)

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    demoSplitInput()
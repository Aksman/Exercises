# EXERCISE
# Create a function that accepts five floating point numbers from user input.

def intakeFloats():
    # Initialize the list of floats
    floats = []

    # By explicitly running until we have five floats, we can handle the situation
    # where the user tries to enter letters, punctuation, or any other non-numeric
    # data. We exit the loop when we have five floats, not just five times through the loop.
    while len(floats) < 5:

        # We use the try-except block to catch a ValueError if the user enters
        # non-numerical data.
        try:
            f = float(input('Enter a floating point number: '))
            floats.append(f)
        except ValueError:
            print('Invalid number. Try again.')

    # We're done, so return the floats.
    return floats

# Example usage
# This block will only run if the script is being run directly (i.e. not imported)
if __name__ == '__main__':
    myNums = intakeFloats()
    print(myNums)
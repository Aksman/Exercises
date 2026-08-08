# EXERCISE
# Create a function that "rotates" a list.

def rotate(lst: list, rotation: int) -> list:
    # Use a modulus ('%') to prevent indexes out of range. 
    # Multiple cycles of rotation are possible.
    rotation = rotation % len(lst)
    # Divide at the rotation index, then switch the two parts.
    # We use the negative of the rotation index because we are
    # defining positive rotation as rightward.
    return lst[-rotation:] + lst[:-rotation]

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    import sys
    rotation = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    myList = sys.argv[2:] if len(sys.argv) > 2 else ['1', '2', '3', '4', '5']

    print(rotate(myList, rotation))
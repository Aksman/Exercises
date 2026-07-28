# EXERCISE
# Create a function that rotates a string a specified number of times.

# Inefficient, loop-y version.
def rotateString1(text: str, rotation: int) -> str:
    direction = 1 if rotation > 0 else -1
    for i in range(1, abs(rotation) + 1):
        if direction == 1:
            c = text[-1]
            text = c + text[:-1]
        else:
            c = text[0]
            text = text[1:] + c
    return text

# More efficient version
def rotateString2(text: str, rotation: int) -> str:
    if rotation > 0: # rightward
        realRotation = rotation % len(text)
        text = text[-realRotation:] + text[:-realRotation]
    else: # leftward
        realRotation = abs(rotation) % len(text)
        text = text[realRotation:] + text[:realRotation] 
    return text
        

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    text = sys.argv[1] if len(sys.argv) > 1 else 'abcdefg'
    rotation = int(sys.argv[2]) if len(sys.argv) > 2 else -9
    rotated1 = rotateString1(text, rotation)
    print(rotated1)

    rotated2 = rotateString2(text, rotation)
    print(rotated2)

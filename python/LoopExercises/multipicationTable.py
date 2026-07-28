# EXERCISE
# Create a function that prints a multiplication table

def printMultTable(lower: int = 1, upper: int = 10):
    width = len(str(upper ** 2))
    # Header
    cols = [' ' * width]
    for i in range(lower, upper + 1):
        cols.append(f"{i:>{width}}")
    print(' '.join(cols))

    # Rows
    for j in range(lower, upper + 1):
        cols = [f"{j:>{width}}"]
        for k in range(lower, upper + 1):
            cols.append(f"{j * k:>{width}}")
        print(' '.join(cols))

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    lower = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    upper = int(sys.argv[2]) if len(sys.argv) > 2 else 10
    printMultTable(lower, upper)

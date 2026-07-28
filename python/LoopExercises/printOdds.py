# EXERCISES
# Create a function to print all odd numbers up to a given number.

def printOdds(limit: int):
    for i in range(1, limit + 1, 2):
        print(f"{i} ", end='')

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 21
    printOdds(limit)
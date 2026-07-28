# EXERCISE
# Create a single multiplication table for a single interview for 1 - 10.

def simpleMultTable(num: int):
    print(f"{'X':>3}{num:>5}")
    for i in range(1, 11):
        print(f"{i:>3}{i * num:>5}")

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    num = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    simpleMultTable(num)
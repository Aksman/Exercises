# EXERCISE
# Create a function that prints a countdown to the screen.
from time import sleep

def countdown(start: int):
    if start > 0:
        start = -start

    while start < 0:
        print(f"T {start} seconds...")
        start += 1
        sleep(1)
    
    print("IGNITION!")

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    n = int(sys.argv[1]) if len(sys.argv) > 1 else -10
    countdown(n)
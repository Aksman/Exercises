# EXERCISE
# Create a function that implements the Collatz conjecture, which states if you start with any
# positive integer, and then divide by 2 if it is even, and multiply by 3 and add 1 if it is odd, 
# repeat, eventually you will reach 1.

def collatzConjecture(num: int) -> list[int]:
    sequence = [num]
    while num != 1:
        if num % 2 == 0:
            num /= 2
        else:
            num = num * 3 + 1
        sequence.append(int(num))
    return sequence

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    num = int(sys.argv[1]) if len(sys.argv) > 1 else 42
    print(f"Original number: {num}")
    print(', '.join([str(i) for i in collatzConjecture(num)]))
        

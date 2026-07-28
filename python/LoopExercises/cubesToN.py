# EXERCISE
# Create a function that outputs a list of the cubes up to a particular integer.

def cubesToN(num: int) -> list[int]:
    cubes = []
    for i in range(1, num + 1):
        cubes.append(i ** 3)
    return cubes

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    num = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    for n in cubesToN(num):
        print(n)
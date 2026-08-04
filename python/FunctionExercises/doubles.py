# EXERCISE
# Use a lambda function with map() to create a function that doubles 
# every number in a list.

def doubles(numbers: list[int]) -> list[int]:
    return list(map(lambda n: n * 2, numbers))

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    import sys
    numbers = sys.argv[1:] if len(sys.argv) > 1 else [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # Convert all the elements in list to ints
    numbers = [int(n) for n in numbers]
    print(doubles(numbers))
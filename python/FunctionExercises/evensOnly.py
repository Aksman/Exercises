# EXERCISE
# Create a function that accepts a list of integers and returns list
# with only the even numbers.
# This demonstrates using a lamba function with filter().

def evensOnly(numbers: list[int]) -> list[int]:
    # The lambda function returns true when the expression n % 2 == 0 is true,
    # i.e. n is an even number. Note that filter() returns an iterator, not a list.
    # We must use list() to convert it into a list before interacting with the contents.
    return list(filter(lambda n: n % 2 == 0, numbers))

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    import sys
    numbers = sys.argv[1:] if len(sys.argv) > 1 else [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # Convert all the elements in list to ints
    numbers = [int(n) for n in numbers]
    print(evensOnly(numbers))
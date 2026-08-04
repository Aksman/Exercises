# EXERCISE
# Define a function that squares a number using a lambda function.
# Lambda functions are useful for quickly defining simple functions.

# The construction is {name} = lambda {arguments}: {expression}
# The result of the expression is what is returned.
sq = lambda x: x * x

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    import sys
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    print(sq(n))
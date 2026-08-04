# EXERCISES
# Create a function to calculate a product of a list of numbers.
# Unlike sum(), there is no ready-made Python function for this.

def product(numbers: list[int|float]) -> int|float: 
    # Initialize our result to 1, since we're multiplying.
    result = 1

    # Loop through the list, multiplying each to the running product
    for n in numbers:
        result *= n

    # Now that we're done, return the product.
    return result

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    def convertNumber(text: str) -> int|float:
        try:
            return int(text)
        except ValueError:
            try:
                return float(text)
            except ValueError:
                raise ValueError(f"Invalid numeric string \"{text}\"")
            
    import sys
    myNumbers = [convertNumber(n) for n in sys.argv[1:]] if len(sys.argv) > 1 else [2, 2, 3, 3, 5, 7]
    print(myNumbers)
    print(product(myNumbers))
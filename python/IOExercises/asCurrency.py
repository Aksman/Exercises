# EXERCISE
# Create a function that outputs a number as currency, complete with
# dollar sign, decimal point with two decimal places, and thousands separator.

def asCurrency(amount: int|float) -> str:
    return f"${amount:,.2f}"

# Example usage
# The following block only runs if the script is accessed directly.
if __name__ == '__main__':
    import sys
    amt = float(sys.argv[1]) if len(sys.argv) > 1 else 15098.75923
    print(asCurrency(amt))
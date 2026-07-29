# EXERCISE
# Create a function that takes a numerator and denominator and returns the ratio
# expressed as a percentage.

def asPercentage(numerator: int, denominator: int) -> str:
    percentage = numerator / denominator * 100
    return f"{percentage:.2f}%"

# Example usage
# The following block will only be run when the script is accessed directly.
if __name__ == '__main__':
    d = int(input('First give me the number of chances in total: '))
    n = int(input('Now give me the number of chances for success: '))
    prob = asPercentage(n, d)
    print(f"The probability is {prob}.")
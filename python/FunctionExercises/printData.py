# EXERCISE
# Create a function that prints off data from a variable length list of 
# keyword-specified arguments. This demonstrates the use of keyword arguments
# (**kwargs) in a function.

def printData(**kwargs):
    # kwargs are imported as a dictionary.
    for k, v in kwargs.items():
        print(f"{k}: {v}")

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    printData(name="Alison Everhart", age=30, city="New York")
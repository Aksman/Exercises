# EXERCISE
# This is a demonstration of the partition string method, which finds a separator string
# and returns a three-part tuple: the part before, the separator itself, and part after.

def splitEmailAddress(address: str) -> tuple:
    return address.partition('@')

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    addy = sys.argv[1] if len(sys.argv) > 1 else 'aksman@example.com'
    # Because the function returns a three value tuple, you can unpack the result in 3 variables.
    name, sep, domain = splitEmailAddress(addy)
    print(name)
    print(sep)
    print(domain)
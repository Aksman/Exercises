# EXERCISE
# Print off an ascii triangle where each row is filled with a successive letter of the alphabet.
# 
# Example:
#
# A
# BB
# CCC
# DDDD
# EEEEE

def printAlphabetTriangle(limit: int):
    if limit <= 0 or limit > 26:
        raise ValueError("Only positive integers between 1 and 26 are allowed.")
    
    # chr(65) = 'A', 
    for i in range(1, limit + 1):
        print(chr(i + 64) * i)

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    printAlphabetTriangle(limit)
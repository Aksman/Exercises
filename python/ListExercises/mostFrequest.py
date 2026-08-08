# EXERCISE
# Return the most frequent value in a list

def mostFrequent(elements: list):
    # Initialize the frequency of each value
    freqs = {}
    # Loop throught the list to count the values
    for el in elements:
        # The .get() method returns the value in the dictionary with the 
        # specified key, or a default value if not found. It works perfectly for 
        # either initializing a new key to a value of one or incrementing it.
        freqs[el] = freqs.get(el, 0) + 1

    val, count = max(freqs.items(), key=lambda item: item[1])
    return val

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    import sys
    myList = sys.argv[1:] if len(sys.argv) > 1 else [1, 8, 6, 7, 2, 5, 2, 2, 4, 2, 7]
    print(mostFrequent(myList))
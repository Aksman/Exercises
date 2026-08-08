# EXERCISE
# Create a function that concatenates the strings in two lists,
# joining them by index.

def zipConcat(list1: list[str], list2: list[str]) -> list[str]:
    # This works because the zip() function combined the two lists into 
    # a single list of tuples, and the list comprehension turns those tuples
    # into single strings.
    return [a + b for a,b in zip(list1, list2)]

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    list1 = ['Th', 'func', 'i', 'surpi', 'sim']
    list2 = ['is', 'tion', 's', 'singly', 'ple']
    print(zipConcat(list1, list2))
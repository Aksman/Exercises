# EXERCISE
# Demonstration of the separator argument in Python's print function

def runExample():
    word1 = input('Give me a word: ')
    word2 = input('Now another word: ')
    word3 = input('One more: ')

    # The "sep" argument of Python's print function allows you to put 
    # any string in place of the default single space. An empty string 
    # is also an option when you want no separation between strings.
    print(word1, word2, word3, sep='***')

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    runExample()
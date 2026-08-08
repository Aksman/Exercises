# EXERCISE
# "Flatten" a multi-dimensional list into a one-dimensional list.

def flatten(lst: list) -> list:
    def isIterable(v):
        try:
            iter(v)
            if isinstance(v, str):
                return False
            else:
                return True
        except TypeError:
            return False
        
    result = []
    for el in lst:
        if isIterable(el):
            result.extend(flatten(el))
        else:
            result.append(el)
    return result

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    #myList = [
    #    [1, 2, [3, 4]],
    #    [[5, 6, [7, 8, 9]], 10, 11],
    #    [12, 13, [[14, [15, 16]], 17], 18, 19, 20]
    #]
    myList = [
        ['apple', 'banana', ['cherry', 'date']],
        [['egg', 'fennel', ['gourd', 'hossenfeffer', 'ice cream']], 'jam', 'kiwi'],
        ['lamb', 'melon', [['nectar', ['orange', 'plum']], 'quiche'], 'rutabega', 'sassafrass', 'tea']
    ]

    flatList = flatten(myList)
    print(flatList)
# EXERCISE
# Create a function that removes items from a dictionary.

def removeKeys(data: dict, keys: list[str]) -> dict:
    # Avoid cycling through a dictionary while removing keys from it.
    # Python throws an error if the size of a dictionary is changed
    # while looping through it. So "for k in data: / if k in keys:" 
    # will not work.
    for k in keys:
        # This is a safer option than del data[k] because it
        # does not return an error if the key is not found.
        # data.pop() returns the value or a default value if not found,
        # but since we don't need it, we won't collect it in a variable.
        data.pop(k, None)

    # The operation is on the original dictionary, but we'll return it anyway        
    return data

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    user = {'name': 'David', 'role': 'admin', 'password': 'e41a2ebf9f071d56697edeb4eeb5f68d6577eea2', 'salt': 'aB'}
    removeKeys(user, ['password', 'salt'])
    print(user)
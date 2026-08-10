# EXERCISE
# Create a function to create a version of a dictionary that only contains certain keys.

def onlyKeys(data: dict, keys: list[str]) -> dict:
    # We use a dictionary comprehension to create a dictionary with 
    # the specified keys. Using "data.get(k, None)" instead of "data[k]"
    # substitutes None for the value if the key is not found in data.
    # Otherwise this would raise an Error.
    return {k: data.get(k, None) for k in keys}

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    user = {
        'name': 'David', 
        'role': 'admin', 
        'password': 'e41a2ebf9f071d56697edeb4eeb5f68d6577eea2', 
        'salt': 'aB',
        'email': 'david@example.com',
        'joined': '2020-08-20'
    }
    publicKeys = ['name', 'role', 'email']
    print("User Info:")
    for k, v in onlyKeys(user, publicKeys).items():
        print(f"{k}: {v}")
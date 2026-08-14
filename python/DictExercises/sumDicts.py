# EXERCISE
# Create a function that combines two or more dictionaries, adding the values together if they share a key.

def sumDicts(*datasets: dict[str, int|float]) -> dict[str, int|float]:
    result = datasets[0].copy()
    for data in datasets[1:]:
        for key, value in data.items():
            result[key] = result.get(key, 0) + value

    return result

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
    dict2 = {'c': 2, 'd': 2}
    dict3 = {'b': 3, 'd': 2, 'f': 1}

    combined = sumDicts(dict1, dict2, dict3)
    for key, value in combined.items():
        print(f"{key}: {value}")

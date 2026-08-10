# EXERCISE
# Create a function that filters entries in a dictionary based on a particular value.

def filterByValue(data: dict[str, int], minimum: int) -> dict[str, int]:
    # We use a dictionary comprehension to return a dictionary 
    # with all the entries that are at least the minimum value.
    return {k: data[k] for k in data if data[k] >= minimum}

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    studentGrades = {
        'Avery Anderson': 100,
        'Brian Bates': 75,
        'Christina Calloway': 88,
        'David Dixon': 94,
        'Ellie Edwards': 92,
        'Frank Fisher': 67,
        'Georgina Guerrero': 85
    }
    passingGrades = filterByValue(studentGrades, 70)

    print('Passing Grades')
    print('-' * 14)
    for student, grade in passingGrades.items():
        print(f"{student}: {grade}")
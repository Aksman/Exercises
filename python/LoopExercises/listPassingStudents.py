# EXERCISE
# Given a dict with a list of students and their grades, along with 
# a passing threshold, return a list of students who passed.

def listPassingStudents(studentGrades: dict, passingThreshold: int = 75):
    # Initialize our list of passing students
    passingStudents = []
    # Use the .items() method to loop through the dict with easy access
    # to both the key (student) and value (grade).
    for student, grade in studentGrades.items():
        if grade >= passingThreshold:
            passingStudents.append(student)
    
    return passingStudents

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        inputItems = sys.argv[1:]
        studentGrades = []
        for item in inputItems:
            student, grade = item.split(':')
            studentGrades[student] = int(grade)
    else:
        studentGrades = {
            'Avery Anderson': 100,
            'Brian Bates': 84,
            'Christina Calloway': 76,
            'David Denton': 72,
            'Ellie Edwards': 91,
            'Fred Fisher': 83,
            'Georgina Guerrero': 96,
            'Hal Hawkins': 79,
            'Isabela Ibanez': 90,
            'James Jackson': 71
        }
    threshold = 75
    print(', '.join(listPassingStudents(studentGrades, 75)))
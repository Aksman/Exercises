# EXERCISE
# Output a list of students and their grades, using the zip() function
# to match a list of students with a list of grades.

def matchStudentsWithGrades(students: list[str], grades: list[int]) ->list[tuple]:
    # The zip() function combines the lists into a single list of tuples. It will cut off 
    # when it reaches the end of one of the lists, making it safer to use than trying to
    # loop through the lists manually.
    return zip(students, grades)

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    students = ['Avery Anderson', 'Brian Bates', 'Christina Calloway', 'David Denton', 'Ellie Edwards']
    grades = [99, 79, 83, 90, 88]
    
    for student, grade in matchStudentsWithGrades(students, grades):
        print(f"{student}: {grade}")
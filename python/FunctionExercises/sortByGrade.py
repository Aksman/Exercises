# EXERCISE
# Create a function that takes a list of tuples that list a student's name and grade,
# and sorts the list based on the grade. 
# This demonstrates sorting of complex data, plus sorting based on a lambda function.

def sortByGrade(studentGrades: list[tuple]) -> list[tuple]:
    # The key parameter of the sorted function allows you to specify a function used
    # for sorting. Here we use a lambda function that takes the tuple and returns the 
    # second (index 1) value, which is the grade. Setting the reverse parameters to True
    # sorts in descending order, with the students with the highest grades listed first.
    return sorted(studentGrades, key=lambda item: item[1], reverse=True)

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    studentGrades = [('Avery Anderson', 100), ('Brian Bates', 88), ('Christina Calloway', 76), ('David Denton', 96), ('Ellie Edwards', 87)]
    print(sortByGrade(studentGrades))
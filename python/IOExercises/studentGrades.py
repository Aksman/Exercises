# EXERCISE
# Create a function that takes a list of students and a list of grades
# and creates a table pairing them.
# This demonstrates stepping through multiple lists simultaneously.

def studentGradesTable(students: list[str], grades: list[int]) -> str:
    # We'll define the column width in one spot here for easy maintainability
    col1Width = 25
    col2Width = 5
    totalWidth = col1Width + col2Width + 1

    # Define the first four lines of the table: 1. a centered caption, 2. a double line,
    # 3. Centered column headers, 4. a single line.
    lines = [
        f"{'STUDENT GRADES':^{totalWidth}}",
        '=' * totalWidth,
        f"{'Student':^{col1Width}}|{'Grade':^{col2Width}}",
        '-' * totalWidth,
    ]
    # Looping through both lists simultaneously
    for i in range(0, len(students)):
        # Next line with student left-aligned and grade right-aligned.
        lines.append(f"{students[i]:<{col1Width}}|{grades[i]:>{col2Width}}")

    # Join all the lines together with new line characters and return the whole table as a string
    return "\n".join(lines)

# Example usage
# This block will only run if the script is being run directly (i.e. not imported)
if __name__ == '__main__':
    import random
    students = ['Avery Anderson', 'Brian Bates', 'Christina Calloway', 'David Denton', 
                'Ellie Edwards', 'Frank Fisher', 'Georgina Guerrero', 'Herman Harris', 
                'Isabela Ibanez', 'James Jackson', 'Kelly Kirkland', 'Lonnie Lipscomb']
    grades = [100] + random.choices(range(74, 100), k=11)
    print(studentGradesTable(students, grades))
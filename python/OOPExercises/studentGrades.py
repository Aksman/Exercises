# EXERCISE
# Create a Student class. This should have a name and a list of test scores.
# There should be a grade() method that determines the student's overall grade.

class Student:
    def __init__(self, name: str, grades: list[int] = []):
        self.name = name
        self.grades = grades

    def addScores(self, *scores: int):
        self.grades.extend(scores)

    def grade(self):
        return round(sum(self.grades) / len(self.grades))

    def letterGrade(self):
        numGrade = self.grade()
        if numGrade < 60:
            return 'F'
        elif numGrade < 70:
            return 'D'
        elif numGrade < 80:
            return 'C'
        elif numGrade < 90:
            return 'B'
        else:
            return 'A'

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    student = Student('Brian Bates', [78, 82, 93])
    student.addScores(85, 87)
    print(f"{student.name} Grade: {student.grade()} ({student.letterGrade()})")
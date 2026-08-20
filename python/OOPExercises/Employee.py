# Define an Employee class with FullTimeEmployee and PartTimeEmployee subclasses.
# The Employee class should have a calculatePaycheck that determines the weekly pay amount,
# with differing criteria for the two subclasses.

class Employee:
    def __init__(self, givenName, surname):
        self.givenName = givenName
        self.surname = surname

    def fullname(self) -> str:
        return f"{self.givenName} {self.surname}"

    def calculatePaycheck(self):
        return 0

class FullTimeEmployee(Employee):
    def __init__(self, givenName, surname, salary):
        super().__init__(givenName, surname)
        self.salary = salary

    def calculatePaycheck(self):
        return self.salary / 52

class PartTimeEmployee(Employee):
    def __init__(self, givenName, surname, rate, hours):
        super().__init__(givenName, surname)
        self.rate = rate
        self.hours = hours

    def calculatePaycheck(self):
        return self.rate * self.hours

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    avery = FullTimeEmployee('Avery', 'Anderson', 120000)
    brian = PartTimeEmployee('Brian', 'Bates', 35, 25)

    print(f"Paycheck for {avery.fullname()}: ${avery.calculatePaycheck():.2f}")
    print(f"Paycheck for {brian.fullname()}: ${brian.calculatePaycheck():.2f}")
# EXERCISE
# Create a program that takes in a list of programs and their version, and produces
# a formatted table with the information.
# This demonstrates text alignments: left, right, and center.

def intakeProgramVersions() -> list[dict]:
    # Preamble
    print('Please provide a list of programs and their versions.')
    print('Enter the name of the program, followed by its version number.')
    print('Enter "/x" to end.')

    # Initialize a list of programs
    programs = []
    # Intake the name of a program and its version number an indeterminate 
    # number of times.
    while True:
        name = input('Program name: ')
        if name == "/x":
            break
        version = input('Version: ')
        if version == "/x":
            break
        programs.append({'name': name, 'version': version})

    return programs

def outputProgramVersions(programs: list[dict]) -> str:
    # Output the table headers:
    # 1. A caption centered above the table 31 characters wide.
    # 2. A line of '=' 31 characters long.
    # 3. The "Name" and "Version" column headers, centered.
    # 4. A line of '-' 31 characters long.
    lines = [
        f"{'LIST OF PROGRAMS':^31}", 
        '=' * 31, 
        f"{'Name':^20}|{'Version':^10}",
        '-' * 31
    ]
    # Output each piece of program data. Left-align the name and 
    # right-align the version.
    for data in programs:
        lines.append(f"{data['name']:<20}|{data['version']:>10}")
    return "\n".join(lines)

# Example usage
# The following block will only be run when the script is accessed directly.
if __name__ == '__main__':
    programs = intakeProgramVersions()
    table = outputProgramVersions(programs)
    print(table)

    



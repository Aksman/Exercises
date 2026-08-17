# EXERCISE
# Create a Notebook class. The class should allow adding notes and listing them.

class Notebook:
    def __init__(self):
        self.notes = []

    def addNote(self, note: str):
        self.notes.append(note)

    def printNotes(self):
        for i, note in enumerate(self.notes, start=1):
            print(f"{i}. {note}")

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    import sys
    notes = sys.argv[1:] if len(sys.argv) > 1 else ['Work out', 'Take out trash', 'Shop for groceries']

    nb = Notebook()
    for note in notes:
        nb.addNote(note)

    print('Notes')
    print('=' * 5)
    nb.printNotes()
# EXERCISE
# Create a function that takes a two-dimenstion list (a list of lists)
# and extends each of its component lists.

def extend2D(map2D: list[list], extension):
    for l in map2D:
        if iter(extension):
            l.extend(extension)
        else:
            l.append(extension)

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    import sys
    ext = sys.argv[1] if len(sys.argv) > 1 else '~'
    map2D = [
        ['~', '~', '~', '~', '~', '~'],
        ['~', 'X', 'X', 'X', 'O', 'O'],
        ['~', 'X', 'X', 'O', 'X', 'X'],
        ['~', 'X', 'X', 'O', 'X', '~'],
        ['~', '~', '~', '~', '~', '~'],
    ]

    extend2D(map2D, ext)

    for row in map2D:
        print(''.join(row))
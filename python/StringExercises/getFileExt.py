# EXERCISE
# Given a file name, return the file extension.
# This can be accomplished in several different ways, and I'll illustrated them here.

# Method #1: pathlib, recommended

from pathlib import Path

def getFileExt1(file: str) -> str:
    path = Path(file)
    return path.suffix

# Method #2: os.path.splitext

import os

def getFileExt2(file: str) -> str:
    root, ext = os.path.splitext(file)
    return ext

# Method #3: Split by '.'
def getFileExt3(file: str) -> str:
    # Split the file name into sections using '.' as the separator. Return the last section.
    sections = file.split('.')
    return '.' + sections[-1]

# Method #4: Find the last '.'
def getFileExt4(file: str) -> str:
    # Find the last '.' in the file name.
    index = file.rfind('.')
    # Slice off everything after the last '.' and return.
    return file[index:]

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    filename = sys.argv[1] if len(sys.argv) > 1 else 'myfilename.ext'
    print(f"File name: {filename}")
    print(f"Method #1: {getFileExt1(filename)}")
    print(f"Method #2: {getFileExt2(filename)}")
    print(f"Method #3: {getFileExt3(filename)}")
    print(f"Method #4: {getFileExt4(filename)}")
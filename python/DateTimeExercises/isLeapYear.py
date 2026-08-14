# EXERCISE
# Create a function that finds if a year (expressed as an integer) is a leap year
# WITHOUT using the calendar module with its isleap() function.

from datetime import datetime

def isLeapYear(year: int) -> bool:
    try:
        # Attempt to create a datetime object representing Feb 29 of the current year.
        dt = datetime(year, 2, 29)
        # If we succeeded, return True.
        return True
    except ValueError:
        # If attempting to create the datetime object raised a ValueError, return False.
        return False

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    import sys
    y = int(sys.argv[1]) if len(sys.argv) > 1 else datetime.now().year
    print(f"{y} is {'not ' if not isLeapYear(y) else ''}a leap year.")
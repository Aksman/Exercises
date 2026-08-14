# EXERCISE
# Create a function that adds a number of weeks from a datetime object,
# and returns the resulting datetime.

from datetime import datetime, timedelta

def addWeeks(dt: datetime, weeks: int) -> datetime:
    # Using a timedelta is an easier and safer option than trying to do the calculations
    # by hand. This works for adding weeks or subtracting weeks (using a negative number here).
    interval = timedelta(weeks=weeks)
    # Conveniently, the "+" and "-" operators work for adding timedeltas to datetime objects.
    return dt + interval

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    import sys
    date = datetime.strptime(sys.argv[1], '%Y-%m-%d') if len(sys.argv) > 1 else datetime.now()
    w = int(sys.argv[2]) if len(sys.argv) > 2 else 4

    newDate = addWeeks(date, w)
    if w > 0:
        print(f"{w} weeks from now it will be {datetime.strftime(newDate, '%B %d, %Y')}.")
    else:
        print(f"{-w} weeks ago it was {datetime.strftime(newDate, '%B %d, %Y')}")
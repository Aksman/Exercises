# EXERCISE
# Create a function that returns the number of days between two dates.

from datetime import datetime

def daysBetween(fromDate: datetime, toDate: datetime) -> int:
    interval = toDate - fromDate
    return interval.days

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    import sys
    fromDate = datetime.strptime(sys.argv[1], '%Y-%m-%d') if len(sys.argv) > 1 else datetime.strptime('2026-08-13', '%Y-%m-%d')
    toDate = datetime.strptime(sys.argv[2], '%Y-%m-%d') if len(sys.argv) > 2 else datetime.strptime('2026-09-09', '%Y-%m-%d')

    days = daysBetween(fromDate, toDate)
    print(f"There are {days} days between {fromDate} and {toDate}.")

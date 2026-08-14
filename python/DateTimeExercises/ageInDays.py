# EXERCISE
# Create a function that will tell how many days ago a specified date way.

from datetime import datetime

def ageInDays(birthdate: datetime) -> int:
    now = datetime.now()
    if birthdate > now:
        raise ValueError('Cannot evaluate base on a future date.')
    diff = now - birthdate
    return diff.days

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    import sys
    date = datetime.strptime(sys.argv[1], '%Y-%m-%d') if len(sys.argv) > 1 else datetime.strptime('1992-09-01', '%Y-%m-%d')
    print(f"You are {ageInDays(date)} days old.")
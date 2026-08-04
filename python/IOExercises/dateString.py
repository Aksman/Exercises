#  EXERCISE
# Given a month, date, and year, create a date string in YYYY-MM-DD format.
# This exercise demonstrates zero-padding.

def dateString(m: int, d: int, y: int) -> str:
    if not 0 < m <= 12:
        raise ValueError('Invalid month.')
    if not 0 < d <= 31:
        raise ValueError('Invalid date.')

    # Note the use of the ':0x' zero-padding format instruction.
    return f"{y:04}-{m:02}-{d:02}"

# Example usage
# This block will only run if the script is being run directly (i.e. not imported)
if __name__ == '__main__':
    myMonth = int(input('Month: '))
    myDate = int(input('Date: '))
    myYear = int(input('Year: '))
    print(dateString(myMonth, myDate, myYear))
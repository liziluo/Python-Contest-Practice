MAX_VALID_YR = 9999
MIN_VALID_YR = 1800
 
# Returns true if given year is valid
def isLeap(year):
     
    # Return true if year
    # is a multiple of 4 and
    # not multiple of 100.
    # OR year is multiple of 400.
    return (((year % 4 == 0) and
             (year % 100 != 0)) or
             (year % 400 == 0))
 
# Returns true if given
# year is valid or not.
def isValidDate(d, m, y):
     
    # If year, month and day
    # are not in given range
    if (y > MAX_VALID_YR or y < MIN_VALID_YR):
        return False
    if (m < 1 or m > 12):
        return False
    if (d < 1 or d > 31):
        return False
 
    # Handle February month
    # with leap year
    if (m == 2):
        if (isLeap(y)):
            return (d <= 29)
        else:
            return (d <= 28)

    if (m == 4 or m == 6 or
        m == 9 or m == 11):
        return (d <= 30)
 
    return True
 
def printPalindromeDates(y1, y2):
     
    # For every year
    for year in range(y1, y2 + 1, 1):
         
        str1 = str(year)
 
        rev = str1
        rev = rev[::-1]
 
        day = int(rev[0 : 2])
        month = int(rev[2 : 4])
 
        rev += str1
        if (isValidDate(day, month, year)):
            print(rev)
 
# Driver code
if __name__ == '__main__':
    y1 = 2000
    y2 = 2100 
    printPalindromeDates(y1, y2)

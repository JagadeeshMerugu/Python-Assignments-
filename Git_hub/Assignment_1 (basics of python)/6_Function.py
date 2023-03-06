year = int(input("Enter a year:"))

def is_leap(year):
    leap = False
    
    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True
            
            else:
                return leap
        else:
            return leap
    return leap
print(is_leap(year))
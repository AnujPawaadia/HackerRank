def is_leap(year):
    if year % 4 == 0:  # Check if the year is divisible by 4
        if year % 100 == 0:  # Check if the year is divisible by 100
            if year % 400 == 0:  # Check if the year is divisible by 400
                return True  # If divisible by 400, it's a leap year
            else:
                return False  # If divisible by 100 but not by 400, not a leap year
        else:
            return True  # If divisible by 4 but not by 100, it's a leap year
    else:
        return False  


year = int(input())
print(is_leap(year))

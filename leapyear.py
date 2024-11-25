def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def find_next_leap_year(year):
    year += 1
    while not is_leap_year(year):
        year += 1
    return year

current_year = int(input("Enter the current year: "))
next_leap_year = find_next_leap_year(current_year)
print(f"The next leap year after {current_year} is {next_leap_year}.")


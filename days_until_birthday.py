# Days Until Birthday Calculator

from datetime import date

month = int(input("Enter your birthday month (1-12): "))
day = int(input("Enter your birthday day (1-31): "))


def days_until_birthday(month, day):

    today = date.today()
    birthday = date(today.year, month, day)

    if birthday < today:
        birthday = birthday.replace(year = today.year + 1)

    remaining = (birthday - today).days
    return remaining
    
days_to_birthday = days_until_birthday(month, day)

if days_to_birthday == 1:
    print(f"There is {days_to_birthday} day remaining until your next birthday!")
else:
    print(f"There are {days_to_birthday} days remaining until your next birthday!")

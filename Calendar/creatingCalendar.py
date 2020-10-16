import calendar

def createCalendar():
    year = int(input("Enter the year: "))
    month = int(input("Enter the month (1-12): "))

    design = calendar.TextCalendar(calendar.SUNDAY)
    userCalendar = design.formatmonth(year, month)

    return userCalendar


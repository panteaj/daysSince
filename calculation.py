from datetime import date

def count():
    start_day = int(input("Enter start day dd: "))
    start_m = int(input("Enter start month mm: "))
    start_y = int(input("Enter start year yyyy: "))

    end_day = int(input("Enter end day dd: "))
    end_m = int(input("Enter end month mm: "))
    end_y = int(input("Enter end year yyyy: "))

    start_date = date(start_y, start_m, start_day)
    end_date = date(end_y, end_m, end_day)

    difference = end_date - start_date

    print("Number of days:", difference.days)

count()

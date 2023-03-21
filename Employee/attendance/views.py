from django.shortcuts import render
import datetime

# Create your views here.


def login(request):
    print("From the console")
    return render(request, 'attendance/first_page.html')


def new_user(request):
    return render(request, 'attendance/new_user.html')


def calender(request):
    current_time = datetime.datetime.now()
    year = current_time.year
    print(year)
    month = current_time.month
    print(month)
    date = current_time.day
    print("Todays date", date)
    total_days = no_of_days_in_a_month(year, month)
    print(total_days)
    total_days_list = {}
    for i in range(0, total_days+1):
        if i==0:
            total_days_list[i] = "date_row_0"
        else:
            total_days_list[i] = "date"
    x_date = datetime.date(year, month, 1)
    no = x_date.weekday()
    no = no
    print(no)
    context = {"year": year, "month": month, "total_days": total_days_list, "week_of_one": no}
    return render(request, 'attendance/calender_ui.html', context)


def no_of_days_in_a_month(y, m):
    leap = 0
    if y % 400 == 0:
        leap = 1
    elif y % 100 == 0:
        leap = 0
    elif y % 4 == 0:
        leap = 1
    if m == 2:
        return 28 + leap
    list = [1, 3, 5, 7, 8, 10, 12]
    if m in list:
        return 31
    return 30

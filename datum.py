day,month = list(map(int,input().strip().split()))
month_day = [31,28,31,30,31,30,31,31,30,31,30,31]
total_days = (day-1)+sum(month_day[:month-1])
day_week = total_days%7

days_week = ["Monday","Tuesday",
        "Wednesday","Thursday",
        "Friday","Saturday","Sunday"]

print(days_week[(3+day_week)%7])

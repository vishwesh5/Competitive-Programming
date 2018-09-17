# problem link: https://www.codechef.com/problems/FLOW015

from datetime import date

def getDay(year):
    d0 = date(2001, 1, 1)
    d1 = date(int(year),1,1)
    days = ["monday",
            "tuesday",
            "wednesday",
            "thursday",
            "friday",
            "saturday",
            "sunday"]
    if (year > 2001):
        delta = d1 - d0
        day = days[delta.days%7]
    else:
        delta = d0 - d1
        day = days[-1*delta.days%7]
    print(day)

for i in range(int(input().strip())):
    getDay(int(input().strip()))

# Cooper Lilly
# UWYO COSC 1010
# Submission Date 11/5/24
# HW 03
# Lab Section: 13
# Sources, people worked with, help given to: 
# your
# comments
# here
import sys

def january_calc (year):
    """find the when january starts"""
    y = year -1
    day = (36+y+(y//4)-(y//100)+(y//400))%7
    return day

def leap_year_local(leap_year):
    """find when its a leap year"""
    if leap_year%400 == 0:
        return True
    elif leap_year%100 == 0:
        return False
    elif leap_year%4 == 0:
        return True
    else:
        return False

raw_date = input("enter date (mm/dd/yyyy)  \n")
enter_date = raw_date.split("/")

mnth_len = {"01":31, "2":28, "3":30, "4":31, "5":30, "6":31, "7":30, "8":31, "9":30, "10":31, "11":30, "12":31}

mnth = enter_date[0]
day = enter_date[1]
year = enter_date[2]

num_days = mnth_len.get(mnth)

if int(mnth) < 1 or int(mnth) >12:
    print(raw_date, "not valid")
    sys.exit()
if int(year) < 1:
    print(raw_date, "not valid")
    sys.exit()
if int(day) > num_days:
    print(raw_date, "not valid")
    sys.exit()


first_day = january_calc(int(year))
is_leap = leap_year_local(int(year))

if is_leap:
    mnth_len["02"] = 29

days = 0
for dict_m, m in mnth_len.items():
    if int(dict_m) < int(mnth):
        days += m
    elif int(dict_m) == int(mnth):
        days += int(day)
        break

day_map = {0:"sunday", 1:"monday", 2:"teusday", 3:"wednesday", 4:"thursday", 5:"friday", 6:"saturday"}
day_of_week = (first_day + days-1) % 7
print(raw_date, day_map[day_of_week])


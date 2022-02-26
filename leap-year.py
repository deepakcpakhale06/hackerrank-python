#!/usr/bin/env python3


def is_leap(year_num):
    leap = False

    if year_num % 4 == 0:
        if year_num % 100 == 0 and year_num % 400 != 0:
            leap = False
        else:
            leap = True
    return leap


year = int(input())
print(is_leap(year))

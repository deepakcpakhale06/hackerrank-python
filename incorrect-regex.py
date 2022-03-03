#!/usr/bin/env python3

import re

if __name__ == '__main__':
    number_of_regex = int(input())
    for regex in range(number_of_regex):
        is_valid_regex = True
        try:
           re.compile(input())
        except re.error:
            is_valid_regex = False
        print(is_valid_regex)



#!/usr/bin/env python3

# Here decorator is used to change the behavior of the original functions
# Decorator invokes the original function just to format the record and returns a iterator object
# iterator object returned by person_listener is simply unpacked
# This implementation is weired because decorator is used to totally modify the behavior of the original function
# Real use of decorators is to enhance the behavior of original function.


def person_lister(f):
    def inner(people):
        # complete the function
        return map(f, sorted(people, key=lambda x: x[2]))

    return inner


@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]


if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')

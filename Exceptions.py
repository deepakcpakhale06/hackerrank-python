#!/usr/bin/env python3

if __name__ == '__main__':
    num_of_tests = int(input())
    for index in range(num_of_tests):
        x, y = input().split()
        try:
            print(int(x)//int(y))
        except Exception as e:
            print(f'Error Code: {e}')

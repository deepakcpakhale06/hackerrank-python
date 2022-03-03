#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Counter is a subclass of Dictionary. Here it is used to convert input string into a Dictionary with characters as keys
# and their occurences values. Also notice that input string is sorted before passing to counter for character counting.
# Index brackets([]) around print statement helps python interpreter identify the expression within itself.
if __name__ == '__main__':
    [print(*c) for c in Counter(sorted(input())).most_common(3)]

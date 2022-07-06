"""
Project Euler Problem 5
=======================

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers
from 1 to 20?
"""

i = 20
found = False
while True:
    print(i, list(map(lambda x: i%x, range(3,21))))
    for x in range(3,21):
        print('x', i, x)
        if i%x != 0:
            continue
    if found:
        break
    i += 20

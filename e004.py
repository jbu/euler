"""
Project Euler Problem 4
=======================

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

from itertools import product

pairs = product(range(100, 1000), range(100, 1000))
prods = [p[0] * p[1] for p in pairs]
pal = [p for p in prods if str(p) == str(p)[::-1]]
print(sorted(pal)[-1])

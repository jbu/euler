"""
Project Euler Problem 3
=======================

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

from typing import Iterator
from itertools import islice

def primes() -> Iterator[int]:
    yield 2
    seen = [2]
    n = 3
    while True:
        for i in seen:
            if n%i != 0:
                continue
        yield n
        n += 2

factors = []
w = 600851475143
piter = primes()
while w > 1:
    p = next(piter)
    if w%p == 0:
        factors.append(p)
        w = w//p
        piter = primes()
print(sorted(factors)[-1])

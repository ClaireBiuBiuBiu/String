'''
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.
Overview
There is a simple way using built-in functions:

Convert a and b into integers.

Compute the sum.

Convert the sum back into binary form.


'''
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return '{0:b}'.format(int(a,2)+int(b,2))
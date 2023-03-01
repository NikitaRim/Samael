"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from collections.abc import Sequence

def check_fibonacci(data: Sequence[int]) -> bool:
    c = 0
    if len(data)>=3:
        for i in range(len(data)-2):
            if data[i]+data[i+1]==data[i+2]:
                c+=1
        if c+2 == len(data):return True
        else: return False
    else: return False
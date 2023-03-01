"""
Classic task, a kind of walnut for you

Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List

def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    """
    :param a: some list of numbers
    :param b: some list of number
    :param c: some list of numbers
    :param d: some list of numbers
    :return: count
    """
    abuba=0
    for i in a:
        for j in b:
            for k in c:
                for z in d:
                    if i+j+k+z == 0:
                        abuba+=1
    return abuba
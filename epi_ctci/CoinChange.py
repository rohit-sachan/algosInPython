""" Infinite coins for some denominations, find all the ways
 n = Dollar value to be achieved
 m = number of denominations
 C = {c0, c1, .... cm-1} denominations of coins

 i.e.
 n=10 , m=4,  C= {2,4,5,3}
 Ans: 7
 explanation:
 22222
 2233
 226
 235
 433
 253
 55

 n=245 m=26
 C={16 30 9 17 40 13 42 5 25 49 7 23 1 44 4 11 33 12 27 2 38 24 28 32 14 50}
 Ans : 64027917156
"""

import sys


def find_ways(arr, total, i, dict):
    if dict.get((total, i)) is not None:
        return dict.get((total, i))

    if total == 0:
        return 1

    elif i >= len(arr):
        return 0

    elif arr[i] > total:
        return find_ways(arr, total, i + 1, dict)

    ways = 0
    inclusion = 0
    while arr[i] * inclusion <= total:
            ways += find_ways(arr, total - (arr[i] * inclusion), i + 1, dict)
            inclusion = inclusion + 1
    dict[(total, i)] = ways
    return ways


def make_change(coins, n):
    return find_ways(coins, n, 0, dict())


n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
coins = [int(coins_temp) for coins_temp in input().strip().split(' ')]
print(make_change(coins, n))

"""
count of subsets to sum
ie. sum =10
set = {1,2,3,5,4,10}

subsets
1,2,3,4
2,3,5
1,5,4
10

ans = 4
"""


def count_sets_from(arr, total, i):
    if total == 0:
        return 1
    elif total < 0:
        return 0
    elif i >= len(arr):
        return 0
    elif total < arr[i]:
        return count_sets_from(arr, total, i + 1)
    else:
        return count_sets_from(arr, total, i+1) + count_sets_from(arr, total-arr[i], i+1)


def count_sets(numbers, n):
    return count_sets_from(numbers, n, 0)


n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
numbers = [int(nos_temp) for nos_temp in input().strip().split(' ')]
print(count_sets(numbers, n))

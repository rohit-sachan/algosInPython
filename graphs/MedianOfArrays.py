def middle_index(ar):
    return int(len(ar) / 2)


def median(ar):
    middle = middle_index(ar)
    if len(ar) % 2 == 0:
        _median = (ar[middle - 1] + ar[middle])/2
    else:
        _median = ar[middle]
    print(_median)
    return _median


def find_median(_ar1, _ar2):
    m1 = median(_ar1)
    m2 = median(_ar2)
    if m1 < m2:
        _ar1 = _ar1[middle_index(_ar1):len(_ar1)]
        _ar2 = _ar2[0:middle_index(_ar2)]

    return 2.4


ar1 = [1, 2, 3, 4, 7]
print(ar1)
ar2 = [5, 6, 9, 10, 11, 13, 16]
print(ar2)
median = find_median(ar1, ar2)
print(median)

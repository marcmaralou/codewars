# You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.

# Examples
# [2, 4, 0, 100, 4, 11, 2602, 36]
# Should return: 11 (the only odd number)

# [160, 3, 1719, 19, 11, 13, -21]
# Should return: 160 (the only even number)

def find_outlier(integers):
    evens = []
    odds = []
    for integer in integers:
        if integer % 2 == 0:
            evens.append(integer)
        if integer % 2 == 1:
            odds.append(integer)
    if len(evens) == 1:
        return evens[0]
    elif len(odds) == 1:
        return odds[0]

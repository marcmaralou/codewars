# Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

# Examples input/output:

# XO("ooxx") => true
# XO("xooxx") => false
# XO("ooxXm") => true
# XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
# XO("zzoo") => false

def xo(s):
    sumX = 0
    sumO = 0
    for char in s:
        if char == "X" or char == "x":
            sumX += 1
        if char == "O" or char == "o":
            sumO += 1
        else:
            continue
    if sumX == sumO:
        return True
    else:
        return False

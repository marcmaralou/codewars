# Simple, given a string of words, return the length of the shortest word(s).

# String will never be empty and you do not need to account for different data types.

def find_short(s):
    x = "alskdfoisjdfoapisjdfoisjodfijsodifjsodifjosidfjosdifjosdifjosidjfsdoif"
    lst = s.split()
    for word in lst:
        if len(word) < len(x):
            x = word
    return len(x)

# Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

# Examples:

# * 'abc' =>  ['ab', 'c_']
# * 'abcdef' => ['ab', 'cd', 'ef']

def solution(s):
    n = 2
    almost = []
    for i in range(0, len(s), n):
        almost.append(s[i:i+n])
    for ele in almost:
        if len(ele) == 1:
            almost.remove(ele)
            almost.append(ele + "_")
    return almost

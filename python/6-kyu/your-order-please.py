# Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

# If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

# Examples
# "is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
# "4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
# ""  -->  ""

def order(sentence):
    list = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
    sentenceList = sentence.split()
    length = len(sentence)
    for word in sentenceList:
        if "1" in word:
            list[0] = word
        elif "2" in word:
            list[1] = word
        elif "3" in word:
            list[2] = word
        elif "4" in word:
            list[3] = word
        elif "9" in word:
            list[8] = word
        elif "5" in word:
            list[4] = word
        elif "6" in word:
            list[5] = word
        elif "7" in word:
            list[6] = word
        elif "8" in word:
            list[7] = word
    answer = " ".join(list)
    return answer[:length]

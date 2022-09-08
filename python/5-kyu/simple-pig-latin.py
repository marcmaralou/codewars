# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

# Examples
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !

def pig_it(text):
    text = text.split()
    list = []
    for word in text:
        if "?" in word:
            list.append(word)
        elif "!" in word:
            list.append(word)
        else:
            pig = word[1:] + word[0] + "ay"
            list.append(pig)
    return " ".join(list)

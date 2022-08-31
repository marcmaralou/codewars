# Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).

# Examples
# "the-stealth-warrior" gets converted to "theStealthWarrior"
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"

import re

def to_camel_case(text):
    text = re.split("-|_", text)
    string = text[0]
    for word in text[1:]:
        string += word.capitalize()
    return string

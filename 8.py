8 lines (7 sloc)  231 Bytes

#Write a Python program to split a string at uppercase letters.
import re
def split(text):
    pattern = r'[A-Z]{1}[a-z]*'
    text = re.findall(pattern, text)
    return text

print(split('ProgramToSplitStringAtUppercaseLetters'))
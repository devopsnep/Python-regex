import re
def find_iter():
    pattern=r"\b\d{5}\b"
    text = "postalcodes are 12345,23456,34567,99876"
    match=re.finditer(pattern,text)
    for i in match:
        print("{} and index at {}".format(i.group(),i.start()))
find_iter()

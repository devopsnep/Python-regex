import re
def groupby():
    pattern=r"(?P<year>\d{4})(?P<month>\d{2})(?P<day>\d{2})"
    text="20171021"
    match=re.finditer(pattern,text)
    for obj in match:
        print(obj.group())
        print(obj.group('year'))
        print(obj.groupdict())

groupby()

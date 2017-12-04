#1 positive look ahead>>>  ?=
#2 negative look ahead>>>  ?!
#3 positive look behind>>> ?<=
#4 negative look behind>>> ?<!
import re
# 1 positive look ahead and non capturing group
string = '''Dec 1.1.1.1 active
Dec     1.2.3.4    active
Dec   2.2.2.2   inactive
Jan 3.3.3.3         active'''
# match only if first column starts with 'Dec' and 3rd column is 'active'
pattern=re.compile('Dec\s+(\S)\s+(?=active)')   # positive look-ahead
result=re.findall(pattern,string)
print(result)
import sys
import re
pattern=r'(?P<timeStamp>\w+\s\w+\s\S+).*to=<(?P<sentTo>\S+)>'
with open(sys.argv[1]) as fh:
    for line in fh:
        match=re.finditer(pattern,line)
        for obj in match:
            dict=obj.groupdict()
            print dict['timeStamp']+ " " +dict['sentTo']

import re
pattern=r'(?P<month>[A-Za-z]{3})\s{1,3}(?P<day>\d{1,2})\s{1,2}(?P<ts>\d+:\d+:\d+).*to=<(?P<email>([\w\.-]+)@([\w\.-]+))'
with open("testmail.txt") as fh1:
    for addr in fh1:
        if addr:
            with open("maillog.txt") as fh:
                for line in fh:
                    if line:
                        match=re.finditer(pattern,line)
                        for obj in match:
                            addr=addr.strip()
                            addr2=obj.group('email').strip()
                            if addr == addr2:
                                print(obj.groupdict('email'))

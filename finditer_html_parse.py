
import re
def find_iter():
    pattern=r'<(?P<heading>h3) class="(?P<class>slide-title)">(?P<result>.*?)<\/\1>'
    file="report.html"
    print(file,"is being opened now")
    with open(file,'r') as fh:
        for line in fh:
            #print(line)
            match=re.finditer(pattern,line)
            for obj in match:
                print("object: ",obj.groupdict())

find_iter()

'''
Group dictionary is main asset: personal note 
output of script:-
    code-2:sandbox ezer$ python3 mytest.py
    report.html is being opened now
    object:  {'heading': 'h3', 'class': 'slide-title', 'result': '72. IZerlandland — GDP per capita: $69,374 (£56,574)'}
    object:  {'heading': 'h3', 'class': 'slide-title', 'result': '99. China — GDP per capita: $69,374 (£56,574)'}
    object:  {'heading': 'h3', 'class': 'slide-title', 'result': '7. japan— GDP per capita: $69,374 (£56,574)'}
'''

import re
def substitue():
    pattern = r"(?P<val_1>\d+(,\d{3})*(\.\d{2})?)\s+dollar(s)?"
    replacement_pattern = r'**USD \g<val_1>**'
    text= \
    ''' Unit cost: 12,000.77 dollars
Tax: 234.98 dollars
Total: 12,234.50 dollars '''
    new_text = re.sub(pattern, replacement_pattern,text)
    print(text)
    print("---------------")
    print(new_text)

substitue()

'''
 \g will use the substring matched by the group named name, as defined by the (?P...) syntax
'''

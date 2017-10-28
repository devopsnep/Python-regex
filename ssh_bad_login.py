#!/Users/ezer/anaconda3/bin/python3
import re
with open("secure.log") as f:
    for line in f:
        str = line
        match = re.findall(r'Failed\spassword\s\w+\s(\w+)\sfrom\s([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})', str,re.IGNORECASE)
        # If-statement after search() tests if it succeeded
        #match is a list with tuples inside. tuples contains regex groups
        #print (match)   #eg value -> [('root', '112.80.40.2')]
        if match:
            #print('found', match.group()) ## 'found word:cat'
            print(match) #[('root', '112.80.40.2')]
            for tups in match:
                for item in tups:
                    print(item)

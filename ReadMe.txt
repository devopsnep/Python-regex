eg. if you want to search hellodev
re.match = looks for the match only at start of string
    it matches "hellodev this is sample" but NOT "this is hellodev sample" "
re.search = looks for match anywhere in the string
    it matches "this is hellodev sample"

Negative look behind:

(?<!spam)@.*
# select all the email where userpart in email doesNOT contain the word spam

Positive look behind:

(?<=spam)@[^;,]+  # this matches below domain part only eg. "zohomail.com"
spam@zohomail.com; spam@google.com; spam@hotmail.com; ram@klsd.com
spam@gmail.com; spam@jira-ya.com,

Positive look ahead
box(?=-shadow)
# matches
    box-shadow
box(?!=-shadow)
    box-testing


#lookahead and look behind in regex
eg. ram@google.com  #lets grab domain "google" only from email
hari@hotmail.edu.np #"hotmail" only
#Positive lookahead =>(?=xxxx) matches a group after your main expression without including it
in the result
@.+(?=\.[a-z]{2,4})



\[(.*)\] #match string between the square brackets []
(cat(dog))  #matches  catdog only
(cat(dog)?) #matches cat or catdog or "cat" part in "dogcat"
(Computer (Scien(ce)?(tist(s)?)?))\b # matches below text
#Computer Science
#Computer Scientists
#Computer Scientist

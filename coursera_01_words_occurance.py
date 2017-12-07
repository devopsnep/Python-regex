name=input("enter file name: ")
handle=open(name,'r')
counts=dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word]=counts.get(word,0) + 1    #here
bigcount=None
bigword=None
print(counts)
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword=word
        bigcount=count
print(bigword,bigcount)
handle.close()

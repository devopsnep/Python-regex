import re
def split_example():
    pattern = r"\d+\.\s*"
    text = 'here is list...1.football 2. tennis 3.basketbal 4.\t\tcricket'
    print(text)
    print('Pattern: {}'.format(pattern))
    split_text=re.split(pattern,text)
    print("Text After Spliting:")
    count=0
    for s in split_text:
        count += 1
        print('{}. {}'.format(count,s))

split_example()

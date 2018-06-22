import re
y=[]
while True:
    x=input()
    if not x:
        break
    regex=re.compile(r'^[\d\w\.-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,4}$')
    response=regex.match(x)
    
    if response:
        y.append(x)
    else:
        print("not valid")
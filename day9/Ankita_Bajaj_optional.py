import re

while True:
    x=input()
    if not x:
        break
    regex = re.compile(r'^[456](\d{15}|\d{3}-(\d{4}-?){3})$')
    response=regex.match(x)
    chk = re.search(r'(\d)\1{3,}',x.replace("-",""))
    
    if response and not chk:
        print("Valid")
    else:
        print("Invalid")
        
        

4123456789123456
5123-4567-8912-3456
61234-567-8912-3456
4123356789123456
5133-3367 -8912-3456
5123 - 3567 - 8912 - 3456

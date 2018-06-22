import re

while True:
    x=input()
    if not x:
        break
    regex = re.compile(r'[-+]?\d*\.\d+$')
    response=regex.match(x)
    
    if response:
        print(True)
    else:
        print(False)
        
        

4  
4.000
-1.00
+4.54
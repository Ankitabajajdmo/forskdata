x=input().split()

if all(int(i)>0 for i in x):
    if any(i[::-1]==i for i in x):
        print(True)
    else:
        print (False)
else:
    print (False)
    
'''
for item in list(map(str,x)):
    if item[::-1] == item:
        yes=1
        break
if yes==1:
    print(True)
else:
    print(False)
''' 
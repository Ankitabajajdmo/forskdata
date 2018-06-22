'''
x=input().split(" ")
y="".join(x)
y=y.lower()
print(y)
for i in range(97,123):
    if str(i) not in y:
        z=1
        
if z==1:
    print("NOT PANGRAM")
else:
    print("PANGRAM")
 '''
       
import string
x=input().split(" ")
y="".join(x)
y=y.lower()
z=0
for i in string.ascii_lowercase:
    if i not in y:
        z=1
if z==1:
    print("NOT PANGRAM")
else:
    print("PANGRAM")
data = input("enter string : ")

d = {}
for i in data:
    d[i] = d.get(i,0)+1
print (d)

'''x=" ".join(data)
y=x.split(" ")
z=list(set(y))
for item in z : 
    print(item,"=",data.count(item))
'''

a=list(set(input("enter string : ")))
lst=[]
for item in a : 
    lst.append((item,data.count(item)))
    
dct = dict(lst)

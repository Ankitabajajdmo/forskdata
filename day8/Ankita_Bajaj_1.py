x=[]
while True:
    a=input()
    if not a:
        break
    y=a.split(",")
    x.append((y[0],int(y[1]),int(y[2])))
x.sort()#(key=lambda x:x[1]) #To sort by first element of the tuple 
print(x)
    

'''   
Tom,19,80 
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
'''

'''
[('John', 20, 90), ('Jony', 17, 91), ('Jony', 17, 93), ('Json', 21, 85), ('Tom', 19, 80)]
'''
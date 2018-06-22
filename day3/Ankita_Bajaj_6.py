nums = list(map(int,input().split(",")))
count = 0
x=0
for item in nums:
    if item == None:
        print(0)
        
    elif item == 13 :
        x=1
        
    else :
        if x==1 :
            x=0            
        else:
            count += item
            
            
print(count)
        
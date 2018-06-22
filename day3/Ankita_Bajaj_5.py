data = list(map(int,input().split(",")))
#data =[1,2,3,4,100]
data.sort()
y=data[1:-1]
print(sum(y)//len(y))

dict1={}
n = int(input())
for i in range(n):
    name = input()
    score = float(input())
    dict1[name]=score
    
print(dict1)

x=(dict1.values()).sort()
print(x)

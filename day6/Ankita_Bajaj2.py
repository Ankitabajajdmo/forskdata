'''
    for i in range(len(x)//2):
        t=x[i]
        x[i]=x[len(x)-i-1]
        x[len(x)-i-1]=t
    return("".join(x))
''' 

def reverse(x):
    return(x[::-1])

x=input()
print(reverse(x))



def add(a,b):
    return a+b

def multiply(a,b):
    return a*b


def largest(a,b):
    if a>b:
        return a
    else :
        return b

def smallest(a,b):
    if a<b:
        return a
    else: 
        return b
    
def sorting(x):
    y=list(x)
    y.sort()
    return(y)
    


def remove_duplicates(x):
    y=list(set(x))
    return y

def Print(x):
    print("sum =",functools.reduce(add,x))
    print("multiply =",functools.reduce(multiply,x))
    print("largest =",functools.reduce(largest,x))
    print("smallest =",functools.reduce(smallest,x))
    print("sorted =",sorting(x))
    print("removed duplicates",remove_duplicates(x))
   
            
    
import functools
x=list(map(int,input().split(",")))
#x=[5,2,6,2,3]
Print(x)
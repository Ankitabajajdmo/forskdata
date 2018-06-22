'''
def can_make(x):
    a,b,c=x
    if c>0:
        if c>1 and c<5:
            if a*1 >=c:
                return "true"
        else:
            p= c//5
            q=c%5
            if q<=a:
                if p*5+q*1==c:
                    return "true"
                else:
                    return "false"
            else:
                return "false"
'''


def can_make(x):
    s,b,g = x
    if g%5 > s:
        return False
    if s+b*5 >= g:
        return True
    else:
        return False

x=list(map(int,input("enter values: ").split(",")))
#x=[2,2,11]
can_make(x)
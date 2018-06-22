'''
def translate(x):
    lst=[]
    
    
    vowles=["a","e","i","o","u"," "]
    for character in x:
        if character not in vowles:
            
           
            
            lst.append(character)
            lst.append("o")
            lst.append(character)
        else:
            lst.append(character)
            
    x=str("".join(lst))
    return x
 '''       
        
def translate(x):
    s=""
    vowles=["a","e","i","o","u"," "]
    for character in x:
        if character not in vowles:
            s=s+character+"o"+character
        else:
            s=s+character
    return s        
        
        
x=input("give input: ")
y=translate(x)
print(y)

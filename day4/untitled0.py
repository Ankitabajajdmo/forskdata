# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 10:18:27 2018

@author: hp


"""

#CONCEPTS OF DICTIONARY
'''
name = 'guru'
number = 99
print('%s %d' % (name,number)	)

x = "Hello World!"
print(x[:6]) 
print(x[0:6] + "Guru99")

oldstring = 'I like Guru99' 
newstring = oldstring.replace('like', 'love')
print(newstring)
print(oldstring)

stri="python at guru99"		
print(stri.upper())

string="python at guru99"
a=string.upper()
print(a)
print(a.lower())
name1 = "geeks"
name2 = "for"
name3 = "geeks"
print(name1.capitalize() + name2.capitalize()
                         + name3.capitalize())

print(":".join("Python"))

string="12345"		
print(':'.join(reversed(string)))

word="guru99 career guru99"		
print(word.split(' '))

word="guru99 career guru99"		
print(word.split('r'))

x = "Guru99"
x.replace("Guru99","Python")
print(x)

x = "Guru99"
x=x.replace("Guru99","Python")
print(x)


a=(5,6)
b=(1,4)
if (a>b):print("a is bigger")
else: print("b is bigger")

a=(5,6)
b=(5,4)
if (a>b):print("a is bigger")
else: print ("b is bigger")

a=(5,6)
b=(6,4)
if (a>b):print("a is bigger")
else: print("b is bigger")
'''
#*******************************
number=(98,46,99,643)
first=("ankita","karishma","joshu","palak")

lst1={}
for contact in first:
    for num in number :
        if first.index(contact)==number.index(num):
            lst1[contact]=num
print(lst1) #DICTIONARY CREATEd VIA TUPLES
print("Telephone Numbers:")
for x in lst1.keys():
    print("Name: ", x, ":",lst1[x])   
    
#*****************************************
    
a = {'x':100, 'y':200}
b = list(a.items())
print(b) 

Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}	
print(Dict['Tiffany'])

Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}	
Boys = {'Tim': 18,'Charlie':12,'Robert':25}
Girls = {'Tiffany':22}	
studentX=Boys.copy()
studentY=Girls.copy()
print(studentX)
print(studentY)

Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}	
x=Dict.update({"Tim":9})
print(Dict)
print(x)

Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}	
del Dict ['Charlie']
print(Dict)

Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}	
print("Students Name: %s" % list(Dict.items()))



Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
Boys = {'Tim': 18,'Charlie':12,'Robert':25}
Girls = {'Tiffany':22}
for key in list(Boys.keys()):
    if key in list(Dict.keys()):
        print(True)
    else:       
        print(False)
        
#*********************
        
Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
Boys = {'Tim': 18,'Charlie':12,'Robert':25}
Girls = {'Tiffany':22}
Students = list(Dict.keys())
Students.sort()
#print(Students)
d={}
for S in Students:
      d[S]=str(Dict[S])#to add key value pair in dictionary
print(d)

#**********************

Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}	
print("Length : %d" % len (Dict))

Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}	
print("variable Type: %s" %type (Dict))

Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
x=str (Dict)	
print("printable string :",x)

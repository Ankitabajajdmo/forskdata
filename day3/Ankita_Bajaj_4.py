data=input("enter data : ")
letter = 0
digit=0

for item in data :
    if item.isalpha():
        letter += 1
    elif  item.isdigit():
        digit += 1
        
print("digit = ",digit,"letter = ",letter)
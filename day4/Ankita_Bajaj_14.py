def valSum(dict1):
    value = 0
    for item in dict1.values():
        if item==15 or item==16:
            value += item
        elif item>12 and item<20:
            item=0
        else:
            value += item
    return value


data=input("enter dictionary: ")
#data='{"a" : 2, "b" : 15, "c" : 13}'

import ast
dict1 = ast.literal_eval(data)

print (valSum(dict1))







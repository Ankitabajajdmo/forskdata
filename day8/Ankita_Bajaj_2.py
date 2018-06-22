from collections import OrderedDict
#d=defaultdict(int)
od = OrderedDict()
while True:
    x=input()
    if not x:
        break
    x = x.split(' ')
    item=' '.join(x[:-1])#This splits content into words, takes all but the last word, and rejoins the words with spaces.
    price = int(x[-1])
    
    od[item]=od.get(item,0)+price

for item,price in od.items():
    print(item,price)
    
    
'''
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30
'''
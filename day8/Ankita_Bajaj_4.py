x=[]
while True:
    e=input()
    if not e:
        break
    if "@" not in e:
        continue
    username, a = e.split("@",1)
    if "@" in a or "." not in a:
        continue
    website,extension= a.rsplit('.',1)
    
    alpha="abcdefghijklmnopqrstuvwxyz0123456789"
    
    if all(c in (alpha+ "-_") for c in username) and all(c in alpha for c in website) and len(extension)<=3 :
        x.append(e)
x.sort()




'''    
ajeet@forsk.com
kunal-23@forsk.com
yogendra_54@forsk.com
'''
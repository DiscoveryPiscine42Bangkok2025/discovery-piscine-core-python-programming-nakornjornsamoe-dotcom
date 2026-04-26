a=input()
alp="abcdefghijklnmopqrstuvwxyz"
r=""
for i in a:
        if i in alp:
            r+=i.upper()
        
        else:
            r+=i.lower() 
print(r)
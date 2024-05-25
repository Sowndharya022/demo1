string=input("enter a string")
d={}
for char in string:
    if char not in d:
        d[char]=1
    else:
        d[char]+=1
        print(char)

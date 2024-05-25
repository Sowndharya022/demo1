string=input("enter a string")
d={}
for char in string:
    d[char]=0
for char in string:
    d[char]=d[char]+1
    print(d)
for char in string:
    if d[char]==1:
        print(char)




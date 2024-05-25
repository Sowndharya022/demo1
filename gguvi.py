sentence =("Guvi Geeks Network Private Limited")
string =(sentence.lower())
count=0
list1=['a','e','i','o','u']
for char in string:
    if char in list1:
        count=count+1
print("no of vowels",count)
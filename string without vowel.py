str=input("enter a string")
vowel_string="aeiouAEIOU"
print("input string",str)
for char in str:
    if char in vowel_string:
        str=str.replace(char,"")
print("output string without vowels",str)
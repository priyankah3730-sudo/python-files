s1 = input("Enter your name: ")
for letter in s1:
    print(letter)
    
    
#printing number times a character based on their position
name = input("Enter your string: ")
for index,letter in enumerate(name): # enumerate data type
    print(letter*(index+1))
    
    
    
    
#to find number of vowels
s = input("Enter your string: ")
count=0
for ch in s:
    if ch in "aeiouAEIOU": 
        count+=1
print("Number of vowels: ",count)
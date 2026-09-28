num = int(input("Enter your number: "))
original=num
reverse = 0
while num>0:
    digit=num%10
    reverse=reverse*10+digit
    num=num//10
if original==reverse:
    print("The number is palindrome")
else:
    print("Number is not palindrome")
    
    

#factorial number
num1 = int(input("Enter your number:"))
fact=1
i=1 
while i<=num1:
    fact=fact*i 
    i=i+1
print(f"Factorial of {num1} is {fact} ")
    
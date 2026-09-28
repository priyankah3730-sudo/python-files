#Counting n numbers
n = int(input("Enter your number: "))
count = 0
while n>0:
    n=n//10
    count=count+1
    
print("Number of digits = ",count)


#Sum of n numbers
n1 = int(input("Enter your number: "))
sum =0
while n1>0:
    digit = n1%10
    sum=sum+digit
    n1=n1//10
print("Sum of digit = ",sum)


#reversing a number using while loop

num = int(input("Enter your number: "))
reverse =0
while num>0:
    digit=num%10
    reverse=reverse*10+digit
    num=num//10
print("Reversed number=", reverse)
num = int(input("Enter the number: "))
if num%5==0:
    print(f" The number {num} is divisible by 5.")
else:
    print(f"The number {num} is not divisible by 5.")
    num = int(input("Enter a number: "))
#The code may even write in one line

num1 = int(input("Enter your number: "))

print("Divisible by 5" if  num1%5==0 else "Not divisible by 5 ")
#1st type
num1 = int(input("Enter a number: "))
last_digit = num1%10
print("The last digit is>>",last_digit)

#2nd type using string
num2 = input("Enter the number: ")
print("the last number is>>", num2[-1])

#3rd way using division
num3 = int(input("Enter a number: "))
last_digit = num3-(num3//10)*10
print("The last digit is>>",last_digit)


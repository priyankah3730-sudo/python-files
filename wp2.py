#printing number from 1 to n
n1 = int(input("Choose one number: "))
i = 1
while i<=n1:
    print(i)
    i=i+1
    
    
#printing sum of n numbers
n2 = int(input("Enter one number: "))
j = 1
sum = 0
while j<=n2:
    sum+=j 
    j+=1
print(f"sum of {n2} numbers is : {sum} ")


#printing multiplication table
n3 = int(input("Enter the number:"))
print("MMultiplication table of number ",n3)
k=1 

while k<=10:
    print(f"{n3}X{k}={n3*k}")
    k=k+1
    
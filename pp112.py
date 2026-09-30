#divtionary comprehensions
names = ["ram","sita","lava","kusha"]
n = {name for name in names}
print (n)
nn = {name:len(name) for name in names}
print(nn)


cp={"bengaluru":99,"chitradurga":67,"hiriyur":78,"mangaluru":87}
lc={key:values for key,values in cp.items() if values>80}
print(lc)


#Squaring the numbers
x=[num for num in range(1,11)]
print(x)
dl=[y**2 for y in x ]
print(dl)
edl=[x1 for x1 in x if x1%2==0]
print(edl)


l=[ y1 for y1 in range(1,6)]
l10=[y2*10 for y2 in l]
print(l10)

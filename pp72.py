L1 = ["priya",1,"riya",2,"kriya",3]
l2 = tuple(L1)
print(l2)
l3 = set(L1)
print(l3)
# it gives error l2.add("muniya")
# (not works) print(l2)
l3.add("muniya")
print(l3) #it adds randomly


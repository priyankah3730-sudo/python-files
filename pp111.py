#list comprehensions
l = [x for x in range(1,11)]
print(l)
dl = [num*2 for num in l]
print(dl)
edl = [x*2 for x in l if x%2==0]
print(edl)


l1 = ["Priyanka","Deepika","Bhoomika","Ramika"]
record = [x[1] for x in l1]
print(record)

record1 = [y1.upper() for y1 in l1]
print(record1)

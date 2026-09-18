s1 = {"Apple","Guava","watermelon"}
s2 = {"Guava","Pomogranate","Mango","Apple"}
print(s1)
print(s1)
print(s2)
print(s1 | s2)
print(s1 & s2)
print(s1 - s2)
print(s2 - s1)

s1.add("Orange")
s2.remove("Mango") #it returns error message if we try to remove element which is not exist
s2.discard("grapes") #if the element doesn't exist it will not return error mrssage
print(s2)
s1.pop() #it may removes any element from set
print(s1)
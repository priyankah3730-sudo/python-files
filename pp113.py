squares={x:x**2 for x in range(1,6)}
print(squares)

cubes={y:y**3 for y in range(1,6)}
print(cubes)


s2={x1:x1**2 for x1 in range(1,7) if x1%2==0}
print(s2)



words=["apple","cat","banana","dog"]
d={word:len(word) for word in words }
print(d)

numbers=[1,2,3,4,5,6,7,8,9,10]
d1={num:"Even" if num%2==0 else "Odd" for num in numbers}
print(d1)
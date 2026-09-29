l=[1,4,5,98,76]
sum=0
for num in l:
    sum= sum+num
print(sum)

#doubling number in the list
l1=l 
dl=[]
for i in l1:
    dl.append(i*2)
print(dl)


#dictionaries
students={"priya":100,"deepu":100,"bhoomi":95}
for  student in students:
    print(student)
    
for mark in students.values():
    print(mark)

#dictionaries
students1=["prema","pallavi","pavitra"]
marks = [89,99,79]
student_marks={}
for index,student in enumerate(students1):
    student_marks[student]=marks[index]
print(student_marks)


for i in range(len(students1)):
    student_marks[students1[i]]=marks[i]
print(student_marks)
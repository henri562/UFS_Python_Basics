students=['Hao','Ruoxi','Iqbal','Jenny']
print(students[0])
print(students[1])
print(students[2])
print(students[3])

print(students[0:4])
print(len(students))

students[2]='Farah'
print(students)

del students[2]
print(students)


students=['Hao','Ruoxi','Iqbal','Pierre']
for student in students:
    print(student)

for i in range(len(students)):
    print('Index %d is %s'%(i,students[i]))

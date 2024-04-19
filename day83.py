from collections import namedtuple

totalStudents = int(input())
columns = input().split()
Student = namedtuple('Student', columns)
totalNumber = 0

for i in range(totalStudents):
    totalNumber += int(Student(*input().split()).MARKS)

print("%.2f" % (totalNumber/totalStudents))

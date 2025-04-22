N = int(input())
students = []
for i in range(N):
    name, g, y, s = input().split()
    students.append([name, int(g), int(y), int(s)])
students.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
for student in students:
    print(student[0])
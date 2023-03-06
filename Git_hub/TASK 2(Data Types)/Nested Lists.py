
        
    
n = int(input())
students = []
for i in range(n):
    name = input()
    grade = float(input())
    students.append([name, grade])


grades = sorted(set([s[1] for s in students]))
second_lowest_grade = grades[1]


names = [s[0] for s in students if s[1] == second_lowest_grade]


for name in sorted(names):
    print(name)

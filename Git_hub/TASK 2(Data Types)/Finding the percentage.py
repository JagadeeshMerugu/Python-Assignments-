if __name__ == '__main__':
    n = int(input("Enter how many number of students records:"))
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input("Enter student name:")
    inp= sum(student_marks[query_name])/len(student_marks[query_name])
    print("average marks","%.2f"%inp)

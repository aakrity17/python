if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    #  WE HAVE TO USE DICTIONARY DS
    for _ in range(n):
        name, *line = input().split()
        # The * is being used to grab additional returns from the split statement.
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print("%.2f" %(sum(student_marks[query_name])/len(student_marks[query_name])))

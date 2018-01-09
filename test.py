import datetime

def text_repo():
    sFile = open("TextRepo/sRepo.txt")
    print("Students:")
    students = []
    i = 0
    for line in sFile:
        line = line[0:len(line)-1]
        students.append(line.split(" "))
        print(students[i])
        i+=1
    aFile = open("TextRepo/aRepo.txt")
    print("Assignments:")
    i = 0
    assignments = []
    for line in aFile:
        line = line[0:len(line)-1]
        assignments.append(line.split(" "))
        a = assignments[i]
        date = a[2].split("-")
        date = datetime.date(int(date[0]), int(date[1]), int(date[2]))
        print(assignments[i], date)
        i+=1
    gFile = open("TextRepo/gRepo.txt")
    grades = []
    i = 0
    for line in gFile:
        line = line[0:len(line)-1]
        grades.append(line.split(" "))
        g = grades[0]
        date = g[3].split("-")
        date = datetime.date(int(date[0]), int(date[1]), int(date[2]))
        print(g, date)
        i+=1
text_repo()

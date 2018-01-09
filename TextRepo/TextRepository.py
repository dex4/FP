from Domain.student import *
from Domain.assignment import *
from Domain.grade import *
import datetime

class TextRepository:
    def __init__(self, studentC, assignmentC, gradeC):
        self.sC = studentC
        self.aC = assignmentC
        self.gC = gradeC
    def getStudents(self):
        sFile = open("TextRepo/sRepo.txt")
        students = []
        i = 0
        for line in sFile:
            line = line[0:len(line)-1]
            students.append(line.split(" "))
            s = students[i]
            stud = Student(int(s[0]), s[1], s[2])
            self.sC.addS(stud)
            for j in range(3, len(s)):
                self.sC.assign_for_student(int(s[0]), s[j])
            i+=1
        sFile.close()
        return self.sC
    def getAssignments(self):
        aFile = open("TextRepo/aRepo.txt")
        i = 0
        assignments = []
        for line in aFile:
            line = line[0:len(line)-1]
            assignments.append(line.split(" "))
            a = assignments[i]
            date = a[2].split("-")
            date = datetime.date(int(date[0]), int(date[1]), int(date[2]))
            asgn = Assignment(a[0], a[1], date)
            self.aC.addA(asgn)
            i+=1
        aFile.close()
        return self.aC
    def getGrades(self):
        gFile = open("TextRepo/gRepo.txt")
        grades = []
        i = 0
        for line in gFile:
            line = line[0:len(line)-1]
            grades.append(line.split(" "))
            g = grades[i]
            date = g[3].split("-")
            date = datetime.date(int(date[0]), int(date[1]), int(date[2]))
            grd = Grade(int(g[0]), g[1], float(g[2]), date)
            self.gC.addG(grd)
            i+=1
        gFile.close()
        return self.gC
    def getData(self):
        self.getStudents()
        self.getAssignments()
        self.getGrades()
    def dumpData(self):
        sFile = open("TextRepo/sRepo.txt", "w")
        lst = self.sC.returnStudentList()
        for s in lst:
            sFile.write(str(s)+"\n")
        sFile.close()
        aFile = open("TextRepo/aRepo.txt", "w")
        lst = self.aC.returnAssignmentList()
        for a in lst:
            aFile.write(str(a)+"\n")
        aFile.close()
        gFile = open("TextRepo/gRepo.txt", "w")
        lst = self.gC.returnGradeList()
        for g in lst:
            gFile.write(str(g)+"\n")
        gFile.close()

import sys
sys.path.append('../')
from Domain.student import *
import pickle
import datetime

class BinRepo:
    def __init__(self, studentC, assignmentC, gradeC):
        self.sC = studentC
        self.aC = assignmentC
        self.gC = gradeC
    def dumpData(self, sC, aC, gC):
        f = open("students.pickle", "wb")
        pickle.dump(self.sC.returnStudentList(), f)
        f.close()
        f = open("assignments.pickle", "wb")
        pickle.dump(self.aC.returnAssignmentList(), f)
        f.close()
        f = open("grades.pickle", "wb")
        pickle.dump(self.gC.returnGradeList(), f)
        f.close()
    def loadStudents(self):
        f = open("students.pickle", "rb")
        for s in pickle.load(f):
            self.sC.addS(s)
        return self.sC
    def loadAssignments(self):
        f = open("assignments.pickle", "rb")
        for a in pickle.load(f):
            self.aC.addA(a)
        return self.aC
    def loadGrades(self):
        f = open("grades.pickle", "rb")
        for g in pickle.load(f):
            self.gC.addG(g)
        return self.gC

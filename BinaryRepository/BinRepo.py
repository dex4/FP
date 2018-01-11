import sys
sys.path.append('../')
from Domain.student import *
import pickle
import datetime
import unittest

class BinRepo:
    def __init__(self, studentC, assignmentC, gradeC, fList):
        self.sC = studentC
        self.aC = assignmentC
        self.gC = gradeC
        self.files = fList
    def dumpData(self, sC, aC, gC):
        f = open(self.files[0], "wb")
        pickle.dump(self.sC.returnStudentList(), f)
        f.close()
        f = open(self.files[1], "wb")
        pickle.dump(self.aC.returnAssignmentList(), f)
        f.close()
        f = open(self.files[2], "wb")
        pickle.dump(self.gC.returnGradeList(), f)
        f.close()
    def loadStudents(self):
        f = open(self.files[0], "rb")
        for s in pickle.load(f):
            self.sC.addS(s)
        return self.sC
    def loadAssignments(self):
        f = open(self.files[1], "rb")
        for a in pickle.load(f):
            self.aC.addA(a)
        return self.aC
    def loadGrades(self):
        f = open(self.files[2], "rb")
        for g in pickle.load(f):
            self.gC.addG(g)
        return self.gC

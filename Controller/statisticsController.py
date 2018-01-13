import sys
sys.path.append('../')
from Controller.assignmentController import *
from Controller.gradeController import *
from Controller.studentController import *

class Statistics:
    def __init__(self, sC, aC, gC):
        self.sController = sC
        self.gController = gC
        self.aController = aC
    def returnStortedStudentsByAvg(self, aID):
        return self.gController.getStudentAvg(self.sController.returnRepo(), aID)
    def returnStortedStudentsAlpha(self, aID):
        return self.gController.getStudentAlpha(self.sController.returnRepo(), aID)
    def getLateStudents(self):
        sList = self.sController.returnStudentList()
        return self.gController.returnLateStudents(sList)
    def bestGrades(self):
        return self.gController.returnGradeStatistic(self.sController.returnRepo())
    def assignmentsByAverage(self):
        return self.gController.returnAssignmentGradeStatistic(self.aController.getRepo())
    def sortStudents(self):
        return self.sController.studentsSorted()

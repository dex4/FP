import sys
sys.path.append('../')
from Controller.assignmentController import *
from Controller.gradeController import *
from Controller.studentController import *

class Statistics:
    def __init__(self, sC, gC, aC):
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

gC = GradeController()

g1 = Grade(12, "A1", 10, datetime.date(2017, 12, 1))
g2 = Grade(12, "A2", 8, datetime.date(2017, 11, 2))
g3 = Grade(13, "A1", 8, datetime.date(2017, 12, 23))
g4 = Grade(14, "A2", 9.33, datetime.date(2017, 10, 23))
gC.addG(g1)
gC.addG(g2)
gC.addG(g3)
gC.addG(g4)
sC = StudentController()
aC = AssignmentController()
stats = Statistics(sC, gC, aC)
s1 = Student(12, "Darjan", "912")
s2 = Student(13, "Andrei", "912")
s3 = Student(14, "Rad", "922")
sC.addS(s1)
sC.addS(s2)
sC.addS(s3)
a1 = Assignment("A1", "Lorem", datetime.date(2017, 12, 1))
a2 = Assignment("A2", "Ipsum", datetime.date(2017, 11, 12))
aC.addA(a1)
aC.addA(a2)
sC.assign_for_group("912", "A1")
sC.assign_for_student(14, "A1")
lst = stats.assignmentsByAverage()
for stud in lst:
    print(stud[0].getID(), stud[1])

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
    def returnStortedStudentsByAvg(self):
        return self.gController.getStudentAvg(self.sController.returnRepo())
    def getLateStudents(self):
        sList = self.sController.returnStudentList()
        aList = self.aController.returnAssignmentList()
        
gC = GradeController()
g1 = Grade(12, "A1", 10, datetime.date(2017, 12, 1))
g2 = Grade(12, "A2", 8, datetime.date(2017, 11, 2))
g3 = Grade(13, "A1", 8, datetime.date(2017, 10, 23))
gC.addG(g1)
gC.addG(g2)
gC.addG(g3)
sC = StudentController()
aC = AssignmentController()
stats = Statistics(sC, gC, aC)
sRepo = stats.sController.returnRepo()
s1 = Student(12, "Darjan", "912")
s2 = Student(13, "Andrei", "912")
sRepo.store(s1)
sRepo.store(s2)
lst = stats.returnStortedStudentsByAvg()
for stud in lst:
    print(stud[0].getName(), stud[1])

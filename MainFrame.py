import sys
sys.path.append('../')
from Controller.assignmentController import *
from Controller.gradeController import *
from Controller.studentController import *
from Controller.statisticsController import *
from display import *

class MainFrame:
    def __init__(self):
        self.sC = StudentController()
        self.aC = AssignmentController()
        self.gC = GradeController()
        self.stats = Statistics(self.sC, self.aC, self.gC)
        g1 = Grade(12, "A1", 10, datetime.date(2017, 12, 1))
        g2 = Grade(12, "A2", 8, datetime.date(2017, 11, 2))
        g3 = Grade(13, "A1", 8, datetime.date(2017, 12, 23))
        g4 = Grade(14, "A2", 9.33, datetime.date(2017, 10, 23))
        self.gC.addG(g1)
        self.gC.addG(g2)
        self.gC.addG(g3)
        self.gC.addG(g4)
        s1 = Student(12, "Darjan", "912")
        s2 = Student(13, "Andrei", "912")
        s3 = Student(14, "Rad", "922")
        self.sC.addS(s1)
        self.sC.addS(s2)
        self.sC.addS(s3)
        a1 = Assignment("A1", "Lorem", datetime.date(2017, 12, 1))
        a2 = Assignment("A2", "Ipsum", datetime.date(2017, 11, 12))
        self.aC.addA(a1)
        self.aC.addA(a2)
        self.sC.assign_for_group("912", "A1")
        self.sC.assign_for_student(14, "A2")
    def workFrame(self, op):
        if(op == "1"):
            what = input("Type S to add a student or A to add an assignment.\n")
            valid = True
            if(what == "S"):
                sID = int(input("Student ID: "))
                sName = input("Name: ")
                sGroup = input("Group: ")
                if(valid == True):
                    s = Student(sID, sName, sGroup)
                    self.sC.addS(s)
            elif(what == "A"):
                aID = input("Assignment ID: ")
                aDesc = input("Assignment description: ")
                aDln = input("Enter deadline, using the YYYY-MM-DD format: ")
                y, m, d = map(int, date_entry.split("-"))
                dln = datetime.date(y, m, d)
                if(valid==True):
                    a = Assignment(aID, aDesc, dln)
                    self.aC.addA(a)
        elif(op == "2"):
            what = input("Type S to delete a student or A to add an assignment.\n")
            valid = True
            if(what == "S"):
                sID = int(input("Student ID: "))
                self.sC.removeStudent(sID)
                self.gC.deleteStudentGrading(sID)
            else:
                aID = input("Assignment ID: ")
                self.aC.deleteAssignment(aID)
                self.gC.deleteAssignmentGrading(aID)
                for student in self.sC.returnStudentList():
                    self.sC.deleteStudentAssignment(student.getID(), aID)
        elif(op == "2"):
            what = input("Type S to delete a student or A to add an assignment.\n")
            valid = True
            if(what == "S"):
                sID = int(input("Student ID: "))
                newName = input("New name: ")
                newGroup = input("New group: ")
                self.sC.updateStudent(sID, newName, newGroup)
            else:
                aID = input("Assignment ID: ")
                newDesc = input("New description: ")
                dln = input("Enter deadline, using the YYYY-MM-DD format: ")
                y, m, d = map(int, date_entry.split("-"))
                newDeadline = datetime.date(y, m, d)
                self.aC.updateAssignment(aID, newDesc, newDeadline)
        elif(op == "4"):#provisionary
            what = input("Type S to delete a student or A to add an assignment.\n")
            if(what == "S"):
                for student in self.sC.returnStudentList():
                    print(student.getID(), student.getName(), student.getGroup())
                    for asgn in student.getAssignmentList():
                        print(asgn)
            else:
                for asgn in self.aC.returnAssignmentList():
                    print(asgn.getID(), asgn.getDescription(), asgn.get_deadline())
    def sList(self):
        return self.sC.returnStudentList()

main = MainFrame()
display = Display()
op = "a"
print(display.printMainMenu())
while(op != "0"):
    op = input("Give option: ")
    main.workFrame(op)

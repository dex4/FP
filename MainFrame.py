import sys
sys.path.append('../')
from Controller.assignmentController import *
from Controller.gradeController import *
from Controller.studentController import *
from Controller.statisticsController import *
from Controller.undo import *
from display import *
import datetime

class MainFrame:
    def __init__(self):
        self.sC = StudentController()
        self.aC = AssignmentController()
        self.gC = GradeController()
        self.stats = Statistics(self.sC, self.aC, self.gC)
        self.undo = Undo(self.sC, self.aC, self.gC)
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
                    self.undo.pushToStack("addS", s.getID())
            elif(what == "A"):
                aID = input("Assignment ID: ")
                aDesc = input("Assignment description: ")
                aDln = input("Enter deadline, using the YYYY-MM-DD format: ")
                y, m, d = map(int, aDln.split("-"))
                dln = datetime.date(y, m, d)
                if(valid==True):
                    a = Assignment(aID, aDesc, dln)
                    self.undo.pushToStack("addA", a.getID())
                    self.aC.addA(a)
        elif(op == "3"):
            what = input("Type S to delete a student or A to delete an assignment.\n")
            valid = True
            if(what == "S"):
                sID = int(input("Student ID: "))
                gradeList = self.gC.returnStudentGrading(sID)
                self.undo.pushToStack("deleteS", (gradeList, self.sC.findStudent(sID)))
                self.sC.removeStudent(sID)
                self.gC.deleteStudentGrading(sID)
            else:
                aID = input("Assignment ID: ")
                gradeList = self.gC.returnAssignmentGrading(aID)
                sList = self.sC.getStudentsWithAssignment(aID)
                self.undo.pushToStack("deleteA", (gradeList, self.aC.returnAssignment(aID), sList))
                self.aC.deleteAssignment(aID)
                self.gC.deleteAssignmentGrading(aID)
                for student in self.sC.returnStudentList():
                    self.sC.deleteStudentAssignment(student.getID(), aID)
        elif(op == "2"):
            what = input("Type S to update a student or A to update an assignment.\n")
            valid = True
            if(what == "S"):
                sID = int(input("Student ID: "))
                newName = input("New name: ")
                newGroup = input("New group: ")
                student = self.sC.findStudent(sID)
                self.undo.pushToStack("updateS", ((student.getID(), student.getName(), student.getGroup()), (sID, newName, newGroup)))
                self.sC.updateStudent(sID, newName, newGroup)
            else:
                aID = input("Assignment ID: ")
                newDesc = input("New description: ")
                dln = input("Enter deadline, using the YYYY-MM-DD format: ")
                y, m, d = map(int, dln.split("-"))
                newDeadline = datetime.date(y, m, d)
                assignment = self.aC.returnAssignment(aID)
                self.undo.pushToStack("updateA", ((assignment.getID(), assignment.getDescription(), assignment.get_deadline()), (aID, newDesc, newDeadline)))
                self.aC.updateAssignment(aID, newDesc, newDeadline)
        elif(op == "4"):
            what = input("Type S to list students or A for assignments.\n")
            if(what == "S"):
                for student in self.sC.returnStudentList():
                    print(student.getID(), student.getName(), student.getGroup())
                    print(student.getAssignmentList())
            else:
                for asgn in self.aC.returnAssignmentList():
                    print(asgn.getID(), asgn.getDescription(), asgn.get_deadline())
        elif(op == "5"):
            aID = input("Give assignment ID: ")
            sID = int(input("Give student ID: "))
            self.undo.pushToStack("ATS", (sID, aID))
            self.sC.assign_for_student(sID, aID)
        elif(op == "6"):
            aID = input("Give assignment ID: ")
            group = input("Give group number: ")
            self.undo.pushToStack("ATG", (group, aID))
            self.sC.assign_for_group(group, aID)
        elif(op == "7"):
            aID = input("Assignment ID: ")
            sID = int(input("Student ID: "))
            grade = float(input("Grade: "))
            turnIn = datetime.datetime.now().date()
            g = Grade(sID, aID, grade, turnIn)
            self.undo.pushToStack("grade", (g.get_student(), g.get_assignment()))
            self.gC.addG(g)
        elif(op == "8"):
            lst = self.gC.returnGradeList()
            for g in lst:
                print(g.get_student(), g.get_assignment(), g.get_grade())
        elif(op == "9"):
            aID = input("Assignment ID: ")
            how = input("Type 'avg' to be sorted by average and 'alpha' to be sorded aplhabetical: ")
            if(how == "avg"):
                lst = self.stats.returnStortedStudentsByAvg(aID)
            else:
                lst = self.stats.returnStortedStudentsAlpha(aID)
            for stud in lst:
                print(stud[0].getID(), stud[0].getName(), stud[1])
        elif(op == "10"):
            lst = self.stats.getLateStudents()
            for stud in lst:
                print(stud[0].getID(), stud[0].getName(), stud[1])
        elif(op == "11"):
            lst = self.stats.bestGrades()
            for stud in lst:
                print(stud[0].getID(), stud[0].getName(), stud[1])
        elif(op == "12"):
            lst = self.stats.assignmentsByAverage()
            for asgn in lst:
                print(asgn[0].getID(), asgn[0].getDescription(), asgn[1])
        elif(op == "undo"):
            self.undo.UndoFrame()
        elif(op == "redo"):
            self.undo.RedoFrame()

main = MainFrame()
display = Display()
op = "a"
print(display.printMainMenu())
while(op != "0"):
    op = input("Give option: ")
    main.workFrame(op)

import sys
sys.path.append('../')
from Controller.assignmentController import *
from Controller.gradeController import *
from Controller.studentController import *
from Controller.statisticsController import *

class Undo:
    def __init__(self, sController, aController, gController):
        self.sC = sController
        self.aC = aController
        self.gC = gController
        self.list = []
    def pushToStack(self, command, params):
        cmd = (command, params)
        self.list.append(cmd)
    def popOutOfStack(self):
        self.list.pop()
    def undoAddS(self, params):
        self.sC.removeStudent(params)
        self.gC.deleteStudentGrading(params)
        self.popOutOfStack()
    def undoUpdateS(self, params):
        self.sC.updateStudent(params[0], params[1], params[2])
        self.popOutOfStack()
    def undoDeleteS(self, params):
        gList = params[0]
        student = params[1]
        self.sC.addS(student)
        for g in gList:
            self.gC.addG(g)
        self.popOutOfStack()
    def undoAddA(self, params):
        self.aC.deleteAssignment(params)
        self.gC.deleteAssignmentGrading(params)
        self.popOutOfStack()
    def undoUpdateA(self, params):
        self.aC.updateAssignment(params[0], params[1], params[2])
        self.popOutOfStack()
    def undoDeleteA(self, params):
        gList = params[0]
        asgn = params[1]
        lst = params[2]
        for student in lst:
            self.sC.assign_for_student(student.getID(), asgn.getID())
        self.aC.addA(asgn)
        for g in gList:
            self.gC.addG(g)
        self.popOutOfStack()
    def undoAssignToStudent(self, params):
        sID = params[0]
        aID = params[1]
        self.sC.deleteStudentAssignment(sID, aID)
        self.popOutOfStack()
    def undoAssignToGroup(self, params):
        group = params[0]
        aID = params[1]
        self.sC.deleteGroupAssignment(group, aID)
        self.popOutOfStack()
    def undoGrading(self, params):
        sID = params[0]
        aID = params[1]
        self.gC.deleteSpecificGrade(sID, aID)
        self.popOutOfStack()
    def mainFrame(self):
        l = len(self.list)
        lst = self.list
        if(l == 0):
            print("No more undos.")
        else:
            cmd = lst[l-1][0]
            params = lst[l-1][1]
            if(cmd == "addS"):
                self.undoAddS(params)
            elif(cmd == "updateS"):
                self.undoUpdateS(params)
            elif(cmd == "deleteS"):
                self.undoDeleteS(params)
            elif(cmd == "addA"):
                self.undoAddA(params)
            elif(cmd == "updateA"):
                self.undoUpdateA(params)
            elif(cmd == "deleteA"):
                self.undoDeleteA(params)
            elif(cmd == "ATS"):
                self.undoAssignToStudent(params)
            elif(cmd == "ATG"):
                self.undoAssignToGroup(params)
            elif(cmd == "grade"):
                self.undoGrading(params)

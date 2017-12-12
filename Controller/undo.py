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
        self.Rlist = []
    def pushToStack(self, command, params):
        cmd = (command, params)
        self.list.append(cmd)
    def popOutOfStack(self):
        self.list.pop()
    def pushToRedo(self, command, params):
        cmd = (command, params)
        self.Rlist.append(cmd)
    def popRedo(self):
        self.Rlist.pop()
    def undoAddS(self, params):
        self.pushToRedo("addS", self.sC.findStudent(params))
        self.sC.removeStudent(params)
        self.gC.deleteStudentGrading(params)
        self.popOutOfStack()
    def undoUpdateS(self, params, redParams):
        self.pushToRedo("updateS", redParams)
        self.sC.updateStudent(params[0], params[1], params[2])
        self.popOutOfStack()
    def undoDeleteS(self, params):
        gList = params[0]
        student = params[1]
        self.sC.addS(student)
        for g in gList:
            self.gC.addG(g)
        self.popOutOfStack()
        self.pushToRedo("deleteS", params)
    def undoAddA(self, params):
        self.pushToRedo("addA", self.aC.returnAssignment(params))
        self.aC.deleteAssignment(params)
        self.gC.deleteAssignmentGrading(params)
        self.popOutOfStack()
    def undoUpdateA(self, params, redParams):
        self.pushToRedo("updateA", redParams)
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
        self.pushToRedo("deleteA", params)
    def undoAssignToStudent(self, params):
        sID = params[0]
        aID = params[1]
        self.sC.deleteStudentAssignment(sID, aID)
        self.popOutOfStack()
        self.pushToRedo("ATS", params)
    def undoAssignToGroup(self, params):
        group = params[0]
        aID = params[1]
        self.sC.deleteGroupAssignment(group, aID)
        self.popOutOfStack()
        self.pushToRedo("ATG", params)
    def undoGrading(self, params):
        sID = params[0]
        aID = params[1]
        self.gC.deleteSpecificGrade(sID, aID)
        self.popOutOfStack()
        self.pushToRedo("grading", params)
    def redoAddS(self, params):
        self.sC.addS(params)
        self.popRedo()
    def redoUpdateS(self, params):
        self.sC.updateStudent(params[0], params[1], params[2])
        self.popRedo()
    def redoAddA(self, params):
        self.aC.addA(params)
        self.popRedo()
    def redoUpdateA(self, params):
        self.aC.updateAssignment(params[0], params[1], params[2])
        self.popRedo()
    def UndoFrame(self):
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
                self.undoUpdateS(params[0], params[1])
            elif(cmd == "deleteS"):
                self.undoDeleteS(params)
            elif(cmd == "addA"):
                self.undoAddA(params)
            elif(cmd == "updateA"):
                self.undoUpdateA(params[0], params[1])
            elif(cmd == "deleteA"):
                self.undoDeleteA(params)
            elif(cmd == "ATS"):
                self.undoAssignToStudent(params)
            elif(cmd == "ATG"):
                self.undoAssignToGroup(params)
            elif(cmd == "grade"):
                self.undoGrading(params)
    def RedoFrame(self):
        l = len(self.Rlist)
        lst = self.Rlist
        if(l == 0):
            print("No more redos.")
        else:
            cmd = lst[l-1][0]
            params = lst[l-1][1]
            if(cmd == "addS"):
                self.redoAddS(params)
            elif(cmd == "addA"):
                self.redoAddA(params)
            elif(cmd == "updateA"):
                self.redoUpdateA(params)
            elif(cmd == "updateS"):
                self.redoUpdateS(params)

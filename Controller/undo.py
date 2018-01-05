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
    def pushToRedo(self, command, params, undParams):
        cmd = (command, params, undParams)
        self.Rlist.append(cmd)
    def popRedo(self):
        self.Rlist.pop()
    def undoAddS(self, params):
        self.pushToRedo("addS", self.sC.findStudent(params), [])
        self.sC.removeStudent(params)
        self.gC.deleteStudentGrading(params)
        self.popOutOfStack()
    def undoUpdateS(self, params, redParams):
        self.pushToRedo("updateS", redParams, params)
        self.sC.updateStudent(params[0], params[1], params[2])
        self.popOutOfStack()
    def undoDeleteS(self, params):
        gList = params[0]
        student = params[1]
        self.sC.addS(student)
        for g in gList:
            self.gC.addG(g)
        self.popOutOfStack()
        self.pushToRedo("deleteS", params, gList)
    def undoAddA(self, params):
        self.pushToRedo("addA", self.aC.returnAssignment(params), [])
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
        self.pushToRedo("deleteA", params, gList)
    def undoAssignToStudent(self, params):
        sID = params[0]
        aID = params[1]
        self.sC.deleteStudentAssignment(sID, aID)
        self.popOutOfStack()
        self.pushToRedo("ATS", params, params)
    def undoAssignToGroup(self, params):
        group = params[0]
        aID = params[1]
        self.sC.deleteGroupAssignment(group, aID)
        self.popOutOfStack()
        self.pushToRedo("ATG", params, params)
    def undoGrading(self, params):
        sID = params[0]
        aID = params[1]
        self.gC.deleteSpecificGrade(sID, aID)
        self.popOutOfStack()
        self.pushToRedo("grading", params, params)
    def redoAddS(self, params):
        self.sC.addS(params)
        self.pushToStack("addS", params.getID())
        self.popRedo()
    def redoUpdateS(self, params, undParams):
        self.sC.updateStudent(params[0], params[1], params[2])
        self.pushToStack("updateS", (undParams, params))
        self.popRedo()
    def redoDeleteS(self, params, undParams):
        self.sC.removeStudent(params[1].getID())
        self.gC.deleteStudentGrading(params[1].getID())
        self.pushToStack("deleteS", params)
        self.popRedo()
    def redoAddA(self, params):
        self.aC.addA(params)
        self.pushToStack("addA", params.getID())
        self.popRedo()
    def redoUpdateA(self, params, undParams):
        self.aC.updateAssignment(params[0], params[1], params[2])
        self.pushToStack("updateA", undParams)
        self.popRedo()
    def redoDeleteA(self, params, undParams):
        lst = params[2]
        for student in lst:
            self.sC.deleteStudentAssignment(student.getID(), params[1].getID())
        self.aC.deleteAssignment(params[1].getID())
        self.gC.deleteAssignmentGrading(params[1].getID())
        self.pushToStack("deleteA", params)
        self.popRedo()
    def redoAssignToStudent(self, params):
        sID = params[0]
        aID = params[1]
        self.sC.assign_for_student(sID, aID)
        self.popRedo()
        self.pushToStack("ATS", params)
    def redoAssignToGroup(self, params):
        group = params[0]
        aID = params[1]
        self.sC.assign_for_group(group, aID)
        self.popRedo()
        self.pushToStack("ATG", params)
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
            uParams = lst[l-1][2]
            if(cmd == "addS"):
                self.redoAddS(params)
            elif(cmd == "addA"):
                self.redoAddA(params)
            elif(cmd == "updateA"):
                self.redoUpdateA(params)
            elif(cmd == "updateS"):
                self.redoUpdateS(params, uParams)
            elif(cmd == "deleteS"):
                self.redoDeleteS(params, uParams)
            elif(cmd == "deleteA"):
                self.redoDeleteA(params, uParams)
            elif(cmd == "ATS"):
                self.redoAssignToStudent(params)
            elif(cmd == "ATG"):
                self.redoAssignToGroup(params)

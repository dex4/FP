import sys
sys.path.append('../')
from Repositories.assignmentRepo import *

class AssignmentController:
    def __init__(self):
        self._aRepo = AssignmentRepo()
    def addA(self, asgn):
        self._aRepo.store(asgn)
    def returnAssignmentList(self):
        return self._aRepo.getAssignmentList()
    def returnAssignment(self):
        return self._aRepo.getAssignment()
    def deleteAssignment(self, aID):
        self._aRepo.remove_assignment(aID)
    def updateAssignment(self, aID, newDesc, newDln):
        self._aRepo.update_assignment(aID, newDesc, newDln)

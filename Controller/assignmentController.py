import sys
sys.path.append('../')
from Repositories.assignmentRepo import *

class AssignmentController:
    def __init__(self):
        self._aRepo = AssignmentRepo()
    def getRepo(self):
        return self._aRepo
    def addA(self, asgn):
        self._aRepo.store(asgn)
    def returnAssignmentList(self):
        return self._aRepo.getAssignmentList()
    def returnAssignment(self, aID):
        return self._aRepo.getAssignment(aID)
    def deleteAssignment(self, aID):
        self._aRepo.remove_assignment(aID)
    def updateAssignment(self, aID, newDesc, newDln):
        self._aRepo.update_assignment(aID, newDesc, newDln)
    def findForValidation(self, aID):
        return self._aRepo.find_for_validation(aID)

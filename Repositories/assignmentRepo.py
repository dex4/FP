import sys
sys.path.append('../')
from Domain.assignment import *
from dataStruct.DataStruct import *
import datetime
import unittest

class AssignmentRepo:
    def __init__(self):
        self._aList = DataStruct()
    def store(self, assignment):
        self._aList.append(assignment)
    def getAssignmentList(self):
        return self._aList.getList()
    def getAssignment(self, aID):
        for asgn in self._aList.getList():
            if(asgn.getID() == aID):
                return asgn
        return None
    def remove_assignment(self, aID):
        aList = self._aList.getList()
        for i in range(0, len(aList)):
            if(aList[i].getID() == aID):
                del self._aList[i]
                break
    def update_assignment(self, aID, newDesc, newDln):
        aList = self._aList.getList()
        for i in range(0, len(aList)):
            if(aList[i].getID() == aID):
                self._aList[i]._description = newDesc
                self._aList[i]._deadline = newDln
                break
    def find_for_validation(self, aID):
        for asgn in self._aList.getList():
            if(asgn.getID() == aID):
                return asgn
        return None

class TestAssignmentRepo(unittest.TestCase):
    def setUp(self):
        self.aRepo = AssignmentRepo()
        self.a1 = Assignment("A1", "Lorem", datetime.date(2017, 12, 1))
        self.a2 = Assignment("A2", "Ipsum", datetime.date(2017, 11, 12))
        self.lst = []
    def test_store(self):
        self.aRepo.store(self.a1)
        self.aRepo.store(self.a2)
        self.assertEqual(self.aRepo._aList, [self.a1, self.a2])
    def test_get(self):
        self.aRepo.store(self.a1)
        self.aRepo.store(self.a2)
        self.assertEqual(self.aRepo.getAssignmentList(), [self.a1, self.a2])
        self.assertEqual(self.aRepo.getAssignment("A1"), self.a1)
        self.assertEqual(self.aRepo.getAssignment("A3"), None)
    def test_removeA(self):
        self.aRepo.store(self.a1)
        self.aRepo.store(self.a2)
        self.aRepo.remove_assignment("A1")
        self.assertEqual(self.aRepo.getAssignmentList(), [self.a2])
    def test_updateA(self):
        self.aRepo.store(self.a1)
        self.aRepo.store(self.a2)
        self.aRepo.update_assignment("A2", "NEW DESCRIPTION", datetime.date(2017, 12, 1))
        a3 = Assignment("A2", "NEW DESCRIPTION", datetime.date(2017, 12, 1))
        self.assertEqual(self.aRepo.getAssignment("A2"), a3)
if __name__ == "__main__":
    unittest.main()

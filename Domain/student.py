import unittest

class Student:
    def __init__(self, ID, Name, grp):
        self._sID = ID
        self._name = Name
        self._group = grp
        self._assignments = []
    def __eq__(self, s):
        if(self._sID == s._sID and self._name == s._name and self._group == s._group):
            return True
        return False
    def addAssignment(self, aID):
        self._assignments.append(aID)
    def getAssignmentList(self):
        return self._assignments
    def getID(self):
        return self._sID
    def getName(self):
        return self._name
    def getGroup(self):
        return self._group

class TestStudent(unittest.TestCase):
    def setUp(self):
        self.s1 = Student("12", "Darjan", "912")
        self.s2 = Student("12", "Drjn", "912")
    def testEquals(self):
        stud1 = Student("12", "Darjan", "912")
        self.assertEqual(self.s1, stud1)
        self.assertNotEqual(self.s1, self.s2)
    def testAddAsgn(self):
        self.s1.addAssignment("A1")
        self.s1.addAssignment("A2")
        assert self.s1.getAssignmentList() == ["A1", "A2"]
    def testGet(self):
        self.assertEqual(self.s1.getID(), "12")
if __name__ == "__main__":
    unittest.main()

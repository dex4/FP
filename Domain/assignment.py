import unittest
import datetime

class Assignment:
    def __init__(self, ID, desc, dln):
        self._aID = ID
        self._description = desc
        self._deadline = dln
    def getID(self):
        return self._aID
    def checkLate(self, turnIn):
        if(turnIn > self._deadline):
            return True
        return False
    def getDescription(self):
        return self._description
    def get_deadline(self):
        return self._deadline
    def __eq__(self, a):
        if(self._aID == a._aID and self._description == a._description and self._deadline == a._deadline):
            return True
        return False
    def __str__(self):
        s = self.getID() + " " + self.getDescription() + " " + str(self.get_deadline())
        return s

class TestAssignment(unittest.TestCase):
    def setUp(self):
        self.a1 = Assignment("A1", "Lorem", datetime.date(2017, 12, 1))
        self.a2 = Assignment("A2", "Ipsum", datetime.date(2017, 11, 12))
    def test_Equality(self):
        asgn = Assignment("A1", "Lorem", datetime.date(2017, 12, 1));
        self.assertTrue(self.a1 == asgn)
        self.assertFalse(self.a2 == asgn)
    def test_get(self):
        asgn = Assignment("A1", "Lorem", datetime.date(2017, 12, 1))
        self.assertEqual(asgn.getID(), "A1")
        self.assertNotEqual(asgn.getID(), "A2")
        self.assertTrue(asgn.getDescription() ==  "Lorem")
        self.assertFalse(asgn.getDescription() =="asd")
        self.assertTrue(asgn.get_deadline() == datetime.date(2017, 12, 1))
        self.assertFalse(asgn.get_deadline() == datetime.date(2017, 12, 2))
    def test_checkEQ(self):
        asgn = Assignment("A1", "Lorem", datetime.date(2017, 12, 1))
        self.assertEqual(asgn.checkLate(datetime.date(2017, 12, 1)), False)
        self.assertNotEqual(asgn.checkLate(datetime.date(2017, 12, 2)), False)

if __name__ == "__main__":
    unittest.main()

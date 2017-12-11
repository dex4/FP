import unittest
import datetime

class Grade:
    def __init__(self, studentID, assignmentID, grd, inDate):
        self._sID = studentID
        self._aID = assignmentID
        self._grade = float(grd)
        self._date = inDate
    def __eq__(self, g):
        if(self._sID == g._sID and self._aID == g._aID and self._grade == g._grade and self._date == g._date):
            return True
        return False
    def get_grade(self):
        return self._grade
    def get_assignment(self):
        return self._aID
    def get_student(self):
        return self._sID
    def get_turnIn(self):
        return self._date

class TestGrade(unittest.TestCase):
    def setUp(self):
        self.g = Grade("12", "A1", 10, datetime.date(2017, 12, 1))
    def testId(self):
        self.assertEqual(self.g._sID, "12")
    def test_get(self):
        grd = self.g
        self.assertEqual(grd.get_grade(), 10)
        self.assertEqual(grd.get_assignment(), "A1")
        self.assertEqual(grd.get_student(), "12")
        self.assertNotEqual(grd.get_turnIn(), datetime.date(2017, 12, 2))
if __name__ == "__main__":
    unittest.main()

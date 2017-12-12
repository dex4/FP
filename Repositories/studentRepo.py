import sys
sys.path.append("../")
from Domain.student import *
from Repositories.assignmentRepo import *
import datetime
import unittest

class StudentRepo:
    """
        This is the repository for students. They are stored in a list.
        The groups list is for validation purposes when adding an assignment.
    """
    def __init__(self):
        self._studentList = []
        self._groups = []
        self._IDs = []
    def store(self, student):
        self._studentList.append(student)
        if(not student._group in self._groups):
            self._groups.append(student._group)
        self._IDs.append(student._sID)
    def get_student_list(self):
        return self._studentList
    def get_groups_list(self):
        return self._groups
    def get_ID_list(self):
        return self._IDs
    def get_assignments(self, sID):
        lst = self._studentList
        for i in range(0, len(lst)):
            if(lst[i]._sID == sID):
                return self._studentList[i].getAssignmentList()
    def remove_student(self, ID):
        lst = self._studentList
        for i in range(0, len(lst)):
            if(lst[i].getID() == ID):
                del self._studentList[i]
                del self._IDs[i]
                break
    def assign_for_student(self, sID, aID):
        lst = self._studentList
        for i in range(0, len(lst)):
            if(lst[i].getID() == sID and lst[i].has_assignment(aID) == False):
                self._studentList[i].addAssignment(aID)
                break
    def assign_for_group(self, group, aID):
        lst = self._studentList
        for i in range(0, len(lst)):
            if(lst[i]._group == group and lst[i].has_assignment(aID) == False):
                self.assign_for_student(lst[i]._sID, aID)
    def find_Student(self, ID):
        lst = self._studentList
        for i in range(0, len(lst)):
            if(lst[i].getID() == ID):
                return lst[i]
            return None
    def update_Student(self, ID, newName, newGroup):
        lst = self._studentList
        for i in range(0, len(lst)):
            if(lst[i].getID() == ID):
                self._studentList[i]._name = newName
                if(newGroup != "0"):
                    self._studentList[i]._group = newGroup
                break
    def delete_student_assignment(self, sID, aID):
        for i in range(0, len(self._studentList)):
            if(self._studentList[i]._sID == sID):
                for j in range(0, len(self._studentList[i]._assignments)):
                    if(self._studentList[i]._assignments[j] == aID):
                        del self._studentList[i]._assignments[j]
                        break
                break
    def delete_group_assignment(self, group, aID):
        for i in range(0, len(self._studentList)):
            if(self._studentList[i]._group == group):
                for j in range(0, len(self._studentList[i]._assignments)):
                    if(self._studentList[i]._assignments[j] == aID):
                        del self._studentList[i]._assignments[j]
                        break
    def students_with_assignment(self, aID):
        lst = self._studentList
        sLst = []
        for student in lst:
            if(aID in student.getAssignmentList()):
                sLst.append(student)
        return sLst
class TestStudentRepo(unittest.TestCase):
    def setUp(self):
        self.sRepo = StudentRepo()
        self.s1 = Student(12, "Darjan", "912")
        self.s2 = Student(13, "Andrei", "912")
        self.s3 = Student(14, "Rad", "931")
        self.s4 = Student(15, "Cristi", "917")
        self.sRepo.store(self.s1)
        self.sRepo.store(self.s2)
        self.sRepo.store(self.s3)
    def test_store(self):
        self.sRepo.store(self.s4)
        self.assertEqual(self.sRepo._studentList, [self.s1, self.s2, self.s3, self.s4])
        self.assertTrue(self.sRepo._groups == ["912", "931", "917"])
        self.assertTrue(self.sRepo._IDs == [12, 13, 14, 15])
        self.assertNotEqual(self.sRepo._studentList, [self.s1, self.s2])
    def test_get(self):
        self.assertEqual(self.sRepo.get_student_list(), [self.s1, self.s2, self.s3])
        self.assertEqual(self.sRepo.get_groups_list(), ["912", "931"])
        self.assertEqual(self.sRepo.get_ID_list(), [12, 13, 14])
    def test_removeS(self):
        self.sRepo.remove_student(13)
        self.assertEqual(self.sRepo.get_student_list(), [self.s1, self.s3])
        self.assertEqual(self.sRepo.get_groups_list(), ["912", "931"])
        self.assertEqual(self.sRepo.get_ID_list(), [12, 14])
    def test_assign(self):
        self.sRepo.assign_for_student(12, "A1")
        self.assertEqual(self.sRepo.get_assignments(12), ["A1"])
        self.sRepo.assign_for_group("912", "A1")
        self.sRepo.assign_for_student(13, "A2")
        self.assertEqual(self.sRepo.get_assignments(12), ["A1"])
        self.assertEqual(self.sRepo.get_assignments(13), ["A1", "A2"])
    def test_update(self):
        self.sRepo.update_Student(12, "Drjn", "944")
        self.sRepo.update_Student(13, "And", "0")
        lst = self.sRepo.get_student_list()
        for i in range(0, len(lst)):
            if(lst[i].getID() == 12):
                self.assertEqual(lst[i].getName(), "Drjn")
                self.assertEqual(lst[i].getGroup(), "944")
            elif(lst[i].getID() == 13):
                self.assertEqual(lst[i].getName(), "And")
                self.assertEqual(lst[i].getGroup(), "912")
    def test_find(self):
        self.assertEqual(self.sRepo.find_Student(12), self.s1)
        self.assertNotEqual(self.sRepo.find_Student(12), self.s2)
        self.assertEqual(self.sRepo.find_Student(34), None)
    def test_get_assignments(self):
        self.sRepo.assign_for_student(12, "A1")
        self.sRepo.assign_for_student(12, "A2")
        self.assertEqual(self.sRepo.get_assignments(12), ["A1", "A2"])
    def test_deleteAssignments(self):
        self.sRepo.assign_for_student(12, "A1")
        self.sRepo.assign_for_student(12, "A2")
        self.sRepo.delete_student_assignment(12, "A1")
        self.assertEqual(self.sRepo.get_assignments(12), ["A2"])
        self.sRepo.assign_for_student(12, "A1")
        self.sRepo.assign_for_student(12, "A2")
        self.sRepo.assign_for_student(13, "A2")
        self.sRepo.delete_group_assignment("912", "A2")
        self.assertEqual(self.sRepo.get_assignments(12), ["A1"])
        self.assertEqual(self.sRepo.get_assignments(13), [])

if __name__ == "__main__":
    unittest.main()

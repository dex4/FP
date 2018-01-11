import sys
sys.path.append('..')
from Domain.grade import *
from Domain.assignment import *
from Domain.student import *
from Repositories.studentRepo import *
from DataStructure.DataStruct import *
import datetime
import unittest

class GradeRepository:
    def __init__(self):
        self._gList = []
    def store(self, grade):
        self._gList.append(grade)
    def get_grade_list(self):
        return self._gList
    def get_specific_grade(self, sID, aID):
        lst = self._gList
        for grade in lst:
            if(grade.get_student() == sID and grade.get_assignment() == aID):
                return grade._grade
    def get_student_grades(self, sID):
        lst = self._gList
        gL = []
        for grade in lst:
            if(grade.get_student() == sID):
                gL.append(grade)
        return gL
    def get_assignment_grades(self, aID):
        lst = self._gList
        gL = []
        for grade in lst:
            if(grade.get_assignment() == aID):
                gL.append(grade)
        return gL
    def get_student_average(self, sID):
        total = 0
        avg = 0
        nr = 0
        if(self.isStudent(sID)):
            for grade in self._gList:
                if(grade.get_student() == sID):
                    total += grade.get_grade()
                    nr += 1
            avg = total/nr
        return avg
    def get_assignment_average(self, aID):
        total = 0
        avg = 0
        nr = 0
        for grade in self._gList:
            if(grade.get_assignment() == aID):
                total += grade.get_grade()
                nr += 1
        avg = total/nr
        return avg
    def isAssignment(self, aID):
        lst = self.get_grade_list()
        for i in range(0, len(lst)):
            if(lst[i].get_assignment() == aID):
                return True
        return False
    def isStudent(self, sID):
        lst = self.get_grade_list()
        for grade in lst:
            if(grade.get_student() == sID):
                return True
        return False
    def delete_assignment_grading(self, aID):
        lst = self.get_grade_list()
        while(self.isAssignment(aID)):
            for i in range(0, len(lst)):
                if(lst[i].get_assignment() == aID):
                    del lst[i]
                    break
    def delete_student_grading(self, sID):
        lst = self.get_grade_list()
        while(self.isStudent(sID)):
            for i in range(0, len(lst)):
                if(lst[i].get_student() == sID):
                    del lst[i]
                    break
    def delete_specific_grade(self, sID, aID):
        lst = self._gList
        for i in range(0, len(lst)):
            if(lst[i].get_student() == sID and lst[i].get_assignment() == aID):
                del lst[i]
                break
    def isGraded(self, sID, aID):
        lst = self.get_grade_list()
        for grade in lst:
            if(grade.get_student() == sID and grade.get_assignment() == aID):
                return True
        return False
    #SORT HERE
    def gradedAssignments(self, asgnList):
        lst = []
        for assignment in asgnList:
            if(self.isAssignment(assignment.getID()) == True):
                avg = self.get_assignment_average(assignment.getID())
                lst.append((assignment.getID(), avg))
        for i in range(0, len(lst)-1):
            for j in range(i+1, len(lst)):
                if(lst[i][1] < lst[j][1]):
                    aux = lst[i]
                    lst[i] = lst[j]
                    lst[j] = aux
        return lst
    #SORT HERE
    def students_by_average(self, studentRepo, aID):
        lst = []
        sRepo = studentRepo
        sList = sRepo.get_student_list()
        newList = []
        for student in sList:
            if(aID in student.getAssignmentList()):
                lst.append(student)
        for student in lst:
            avg = self.get_student_average(student.getID())
            if(avg != 0):
                newList.append((student, avg))
        for i in range(0, len(sList)-1):
            for j in range(i+1, len(newList)):
                if(newList[i][1] < newList[j][1]):
                    aux = newList[i]
                    newList[i] = newList[j]
                    newList[j] = aux
        return newList
    def student_alphabetical(self, studentRepo, aID):
        lst = []
        sRepo = studentRepo
        sList = sRepo.get_student_list()
        newList = []
        for student in sList:
            if(aID in student.getAssignmentList()):
                lst.append(student)
        for student in lst:
            avg = self.get_student_average(student.getID())
            if(avg != 0):
                newList.append((student, avg))
        for i in range(0, len(newList)-1):
            for j in range(i+1, len(newList)):
                if(newList[i][0].getName() > newList[j][0].getName()):
                    aux = newList[i]
                    newList[i] = newList[j]
                    newList[j] = aux
        return newList
    def isLate(self, student):
        lst = student.getAssignmentList()
        sID = student.getID()
        for asgn in lst:
            if(not self.isGraded(sID, asgn)):
                return True
        print("LATE!")
        return False
    def get_late_students(self, sList):
        lst = self.get_grade_list()
        lateList = []
        for i in range(0, len(sList)):
            student = sList[i]
            assignments = sList[i].getAssignmentList()
            for j in range(0 ,len(assignments)):
                if((not self.isGraded(student.getID(), assignments[j])) and self.isLate(student)):
                    lateList.append((student, assignments[j]))
        return lateList
    #SORT HERE
    def sort_students_by_grade(self, studentRepo):
        sRepo = studentRepo
        sList = sRepo.get_student_list()
        newList = []
        for student in sList:
            avg = self.get_student_average(student.getID())
            newList.append((student, avg))
        for i in range(0, len(newList)-1):
            for j in range(i+1, len(newList)):
                if(newList[i][1] < newList[j][1]):
                    aux = newList[i]
                    newList[i] = newList[j]
                    newList[j] = aux
        return newList
    def sort_assignments_by_average(self, asgnRepo):
        aRepo = asgnRepo
        aList = aRepo.getAssignmentList()
        newList = []
        for assignment in aList:
            avg = self.get_assignment_average(assignment.getID())
            newList.append((assignment, avg))
        for i in range(0, len(newList)-1):
            for j in range(i+1, len(newList)):
                if(newList[i][1] < newList[j][1]):
                    aux = newList[i]
                    newList[i] = newList[j]
                    newList[j] = aux
        return newList
class TestGrade(unittest.TestCase):
    def setUp(self):
        self.gRepo = GradeRepository()
        self.g1 = Grade(12, "A1", 10, datetime.date(2017, 12, 1))
        self.g2 = Grade(12, "A2", 8, datetime.date(2017, 11, 2))
        self.g3 = Grade(13, "A1", 8, datetime.date(2017, 10, 23))
        self.gRepo.store(self.g1)
        self.gRepo.store(self.g2)
        self.gRepo.store(self.g3)
    def test_store(self):
        self.gRepo.store(self.g1)
        self.assertEqual(self.gRepo._gList, [self.g1, self.g2, self.g3, self.g1])
        self.assertNotEqual(self.gRepo._gList, [])
    def test_get(self):
        self.assertEqual(self.gRepo.get_grade_list(), [self.g1, self.g2, self.g3])
        self.assertEqual(self.gRepo.get_specific_grade(12, "A1"), 10)
        self.assertEqual(self.gRepo.get_student_average(12), 9.0)
        self.assertEqual(self.gRepo.get_assignment_average("A1"), 9)
    def test_isAssignment(self):
        self.assertTrue(self.gRepo.isAssignment("A1"))
        self.assertFalse(self.gRepo.isAssignment("A3"))
    def test_isStudent(self):
        self.assertTrue(self.gRepo.isStudent(12))
        self.assertFalse(self.gRepo.isAssignment(24))
    def test_isGraded(self):
        self.assertTrue(self.gRepo.isGraded(12, "A1"))
        self.assertFalse(self.gRepo.isGraded(13, "A2"))
    def test_deletion(self):
        self.gRepo.delete_student_grading(12)
        self.assertEqual(self.gRepo.get_grade_list(), [self.g3])
        self.gRepo.store(self.g1)
        self.gRepo.store(self.g2)
        self.gRepo.delete_assignment_grading("A1")
        self.assertEqual(self.gRepo.get_grade_list(), [self.g2])
        self.gRepo.store(self.g1)
        self.gRepo.store(self.g3)
        self.gRepo.delete_specific_grade(12, "A1")
        self.assertEqual(self.gRepo.get_grade_list(), [self.g2, self.g3])
    def test_gradedAssignments(self):
        a1 = Assignment("A1", "Lorem", datetime.date(2017, 12, 1))
        a2 = Assignment("A2", "Ipsum", datetime.date(2017, 11, 12))
        self.assertEqual(self.gRepo.gradedAssignments([a1, a2]), [("A1", 9), ("A2", 8)])
    def test_sortAvg(self):
        sRepo = StudentRepo()
        s1 = Student(12, "Darjan", "912")
        s2 = Student(13, "Andrei", "912")
        sRepo.store(s1)
        sRepo.store(s2)
        lst = self.gRepo.students_by_average(sRepo, "A1")
        self.assertEqual(lst, [])
    def test_getSG(self):
        self.assertEqual(self.gRepo.get_student_grades(12), [self.g1, self.g2])

if __name__ == "__main__":
    unittest.main()

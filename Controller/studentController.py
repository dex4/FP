import sys
sys.path.append("../")
from Repositories.studentRepo import *
import unittest

class StudentController:
    def __init__(self):
        self._sRepo = StudentRepo()
    def returnRepo(self):
        return self._sRepo
    def addS(self, student):
        self._sRepo.store(student)
    def returnStudentList(self):
        return self._sRepo.get_student_list()
    def returnGroupsList(self):
        return self._sRepo.get_groups_list()
    def returnIDList(self):
        return self._sRepo.get_ID_list()
    def returnAssignments(self, sID):
        return self._sRepo.get_assignments(sID)
    def removeStudent(self, sID):
        self._sRepo.remove_student(sID)
    def assign_for_student(self, sID, aID):
        self._sRepo.assign_for_student(sID, aID)
    def assign_for_group(self, group, aID):
        self._sRepo.assign_for_group(group, aID)
    def findStudent(self, sID):
        return self._sRepo.find_Student(sID)
    def updateStudent(self, sID, newName, newGroup):
        self._sRepo.update_Student(sID, newName, newGroup)
    def deleteStudentAssignment(self, sID, aID):
        self._sRepo.delete_student_assignment(sID, aID)
    def deleteGroupAssignment(self, group, aID):
        self._sRepo.delete_group_assignment(group, aID)
    def getStudentsWithAssignment(self, aID):
        return self._sRepo.students_with_assignment(aID)
    def findForValidation(self, sID):
        return self._sRepo.find_for_validation(sID)
    def studentsSorted(self):
        return self._sRepo.alphaSorted()
    def filterForGroup(self, group):
        return self._sRepo.filteredByGroup(group)

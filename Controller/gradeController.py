import sys
sys.path.append('../')
from Repositories.gradeRepo import *

class GradeController:
    def __init__(self):
        self._gRepo = GradeRepository()
    def addG(self, grade):
        self._gRepo.store(grade)
    def returnGradeList(self):
        return self._gRepo.get_grade_list()
    def returnSpecificGrade(self, sID, aID):
        return self._gRepo.get_specific_grade(sID, aID)
    def studentAverage(self, sID):
        return self._gRepo.get_student_average(sID)
    def assignmentAverage(self, aID):
        return self._gRepo.get_assignment_average(aID)
    def isAssignmentGraded(self, aID):
        return self._gRepo.isAssignment(aID)
    def isStudentGraded(self, sID):
        return self._gRepo.isStudent(sID)
    def deleteAssignmentGrading(self, aID):
        self._gRepo.delete_assignment_grading(aID)
    def deleteStudentGrading(self, sID):
        self._gRepo.delete_student_grading(sID)
    def deleteSpecificGrade(self, sID, aID):
        self._gRepo.delete_specific_grade(sID, aID)
    def findGrade(self, sID, aID):
        return self._gRepo.isGraded(sID, aID)
    def getGradedAssignments(self, asgnList):
        return self._gRepo.gradedAssignments(asgnList)

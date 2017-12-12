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
    def getStudentAvg(self, sRepo, aID):
        return self._gRepo.students_by_average(sRepo, aID)
    def getStudentAlpha(self, sRepo, aID):
        return self._gRepo.student_alphabetical(sRepo, aID)
    def returnLateStudents(self, sList):
        return self._gRepo.get_late_students(sList)
    def returnGradeStatistic(self, sRepo):
        return self._gRepo.sort_students_by_grade(sRepo)
    def returnAssignmentGradeStatistic(self, aRepo):
        return self._gRepo.sort_assignments_by_average(aRepo)
    def returnStudentGrading(self, sID):
        return self._gRepo.get_student_grades(sID)
    def returnAssignmentGrading(self, aID):
        return self._gRepo.get_assignment_grades(aID)

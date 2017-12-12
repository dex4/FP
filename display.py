import sys
sys.path.append('../')
import datetime
from Repositories.Exception import *
from Repositories.studentRepo import *
class Display:
    def printMainMenu(self):
        s = "1.Add student/assignment.\n2.Update student/assignment.\n3.Remove student/assignment.(REQ: undo)\n4.List students/assignments.\n"
        s += "5.Give assignment to a student.\n6.Give assignment to a group of students."
        s += "\n7.Grade a student.(REQ: validation)\n8.List grades.\n"
        s += "\nSTATISTICS OPTIONS:\n"
        s += "\n9.List students who recieved a given assignment.\n10.Late in turning in at least an assignment.\n11.List students sorted by school situation.\n12.List assignments with at least one grade."
        s += "\n13. Undo.\n14.Redo (TBI)\n"
        return s

    def getInput(self):
        op = input("Pick option: ")
        try:
            int(op)
        except ValueError:
            print("Option should be a number from 1 to 12.")
            return
        try:
            if(int(op) < 0 or int(op) > 14):
                raise RepositoryException("Option should be a number from 1 to 12.")
        except RepositoryException as e:
            print(e)
            return
        return op

    def getAddStudent(self):
        print("Give the student's details:")
        ID = input("ID: ")
        name = input("Name: ")
        group = input("Group: ")
        return (ID, name, group)

    def getUpdateStudent(self):
        ID = input("ID: ")
        name = input("New name: ")
        group = input("New group (type 0 to leave unchanged): ")
        return (ID, name, group)

    def getRemoveStudent(self):
        ID = input("Give the ID of the student you want removed: ")
        return ID
    #<---Assignments--->

    def getAddAssignment(self):
        print("Give the assignment's details:")
        ID = input("ID: ")
        desc = input("Description: ")
        date_entry = input("Enter deadline, using the YYYY-MM-DD format: ")
        y, m, d = map(int, date_entry.split("-"))
        dln = datetime.date(y, m, d)
        return (ID, desc, dln)

    def getUpdateAssignment(self):
        ID = input("ID: ")
        desc = input("New description: ")
        deadline = input("New deadline: ")
        return (ID, desc, deadline)

    def getRemoveAssignment(self):
        ID = input("Give the ID of the assignment you want removed: ")
        return ID

    #<---Giving an assignment --->
    def assignToStudent(self):
        aID = input("Assignment's ID: ")
        sID = input("Student's ID you want it assigned to: ")
        return (sID, aID)

    def assignToGroup(self):
        aID = input("Assignment's ID: ")
        group = input("Group number: ")
        return (group, aID)
    #<--- Grading --->
    def getGrading(self):
        sID = input("Student's ID: ")
        aID = input("Assignment's ID: ")
        grade = input("Grade: ")
        turnin = self.getTurnInDate()
        return (sID, aID, grade, turnin)

    def getTurnInDate(self):
        date_entry = input("Enter turn in date, using the YYYY-MM-DD format: ")
        y, m, d = map(int, date_entry.split("-"))
        turnin = datetime.date(y, m, d)
        return (turnin)

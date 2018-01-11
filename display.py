import sys
sys.path.append('../')
import datetime
from Repositories.Exception import *
from Repositories.studentRepo import *

class Display:
    def __init__(self, sController, aController, gController):
        self.sC = sController
        self.aC = aController
        self.gC = gController
    def printMainMenu(self):
        s = "1.Add student/assignment.\n2.Update student/assignment.\n3.Remove student/assignment.\n4.List students/assignments.\n"
        s += "5.Give assignment to a student.\n6.Give assignment to a group of students."
        s += "\n7.Grade a student.(REQ: validation)\n8.List grades.\n"
        s += "\nSTATISTICS OPTIONS:\n"
        s += "\n9.List students who recieved a given assignment.\n10.Late in turning in at least an assignment.\n11.List students sorted by school situation.\n12.List assignments with at least one grade."
        s += "\n13.Undo.\n14.Redo\n0.Exit\n"
        return s

    def getInput(self):
        op = input("Pick option: ")
        if(op == "undo" or op == "redo"):
            return op
        try:
            int(op)
        except ValueError:
            print("Option should be a number from 1 to 12.")
            return
        try:
            if(int(op) < 0 or int(op) > 14):
                raise EntryException("Option should be a number from 1 to 12.")
        except EntryException as e:
            print(e)
            return
        return op

    def getAddStudent(self):
        print("Give the student's details:")
        ID = input("ID: ")
        try:
            int(ID)
        except ValueError:
            print("ID should be an integer number")
            return False
        try:
            if(self.sC.findForValidation(int(ID)) != Student(1, "n", "n")):
                raise EntryException("Student ID already exists!")
        except EntryException as e:
            print(e)
            return False
        name = input("Name: ")
        group = input("Group: ")
        return (int(ID), name, group)

    def getUpdateStudent(self):
        ID = input("ID: ")
        try:
            int(ID)
        except ValueError:
            print("ID should be an integer number")
            return False
        try:
            if(self.sC.findForValidation(int(ID)) == Student(1, "n", "n")):
                raise EntryException("Student ID doesn't exist!")
        except EntryException as e:
            print(e)
            return False
        name = input("New name: ")
        group = input("New group (type 0 to leave unchanged): ")
        return (int(ID), name, group)

    def getRemoveStudent(self):
        ID = input("Give the ID of the student you want removed: ")
        try:
            int(ID)
        except ValueError:
            print("ID should be an integer number")
            return False
        try:
            if(self.sC.findForValidation(int(ID)) == Student(1, "n", "n")):
                raise EntryException("Student ID doesn't exist!")
        except EntryException as e:
            print(e)
            return False
        return int(ID)
    #<---Assignments--->

    def getAddAssignment(self):
        print("Give the assignment's details:")
        ID = input("ID: ")
        try:
            if(self.aC.findForValidation(ID) != Assignment("!", "!", "!")):
                raise EntryException("Assignment ID already exists!")
        except EntryException as e:
            print(e)
            return False
        desc = input("Description: ")
        date_entry = input("Enter deadline, using the YYYY-MM-DD format: ")
        try:
            vy = date_entry[0:3]
            vm = date_entry[5:6]
            vd = date_entry[8:9]
            int(vy)
            int(vm)
            int(vd)
        except ValueError:
            print("Invalid date. Try again.")
            return False
        y, m, d = map(int, date_entry.split("-"))
        dln = datetime.date(y, m, d)
        return (ID, desc, dln)

    def getUpdateAssignment(self):
        ID = input("ID: ")
        try:
            if(self.aC.findForValidation(ID) == Assignment("!", "!", "!")):
                raise EntryException("Assignment ID doesn't exist!")
        except EntryException as e:
            print(e)
            return False
        desc = input("New description: ")
        date_entry = input("New deadline: ")
        try:
            vy = date_entry[0:3]
            vm = date_entry[5:6]
            vd = date_entry[8:9]
            int(vy)
            int(vm)
            int(vd)
        except ValueError:
            print("Invalid date. Try again.")
            return False
        return (ID, desc, date_entry)

    def getRemoveAssignment(self):
        ID = input("Give the ID of the assignment you want removed: ")
        try:
            if(self.aC.findForValidation(ID) == Assignment("!", "!", "!")):
                raise EntryException("Assignment ID doesn't exist!")
        except EntryException as e:
            print(e)
            return False
        return ID

    #<---Giving an assignment --->
    def assignToStudent(self):
        aID = input("Assignment's ID: ")
        try:
            if(self.aC.findForValidation(aID) == Assignment("!", "!", "!")):
                raise EntryException("Assignment ID doesn't exist!")
        except EntryException as e:
            print(e)
            return False
        sID = input("Student's ID you want it assigned to: ")
        try:
            int(sID)
        except ValueError:
            print("ID should be an integer number")
            return False
        try:
            if(self.sC.findForValidation(int(sID)) == Student(1, "n", "n")):
                raise EntryException("Student ID doesn't exist!")
        except EntryException as e:
            print(e)
            return False
        return (int(sID), aID)

    def assignToGroup(self):
        aID = input("Assignment's ID: ")
        try:
            if(self.aC.findForValidation(aID) == Assignment("!", "!", "!")):
                raise EntryException("Assignment ID doesn't exist!")
        except EntryException as e:
            print(e)
            return False

        group = input("Group number: ")
        return (group, aID)
    #<--- Grading --->
    def getGrading(self):
        sID = input("Student's ID: ")
        try:
            int(sID)
        except ValueError:
            print("ID should be an integer number")
            return False
        try:
            if(self.sC.findForValidation(int(sID)) == Student(1, "n", "n")):
                raise EntryException("Student ID doesn't exist!")
        except EntryException as e:
            print(e)
            return False
        sID = int(sID)
        aID = input("Assignment's ID: ")
        try:
            if(self.aC.findForValidation(aID) == Assignment("!", "!", "!")):
                raise EntryException("Assignment ID doesn't exist!")
        except EntryException as e:
            print(e)
            return False
        try:
            if(self.gC.is_graded(sID, aID) == True):
                raise EntryException("Assignment is already graded.")
        except EntryException as e:
            print(e)
            return False
        try:
            lst = self.sC.returnAssignments(sID)
            if(not aID in lst):
                raise EntryException("Student does not have this assignment.")
        except EntryException as e:
            print(e)
            return False
        grade = input("Grade: ")
        try:
            float(grade)
        except ValueError:
            print("The grade should be a real number!")
            return False
        try:
            grade = float(grade)
            if(grade < 0 or grade > 10):
                raise EntryException("Grade should be a number between 1 and 10.")
        except EntryException as e:
            print(e)
            return False
        turnin = self.getTurnInDate()
        return (sID, aID, grade, turnin)

    def getTurnInDate(self):
        date_entry = input("Enter turn in date, using the YYYY-MM-DD format: ")
        y, m, d = map(int, date_entry.split("-"))
        turnin = datetime.date(y, m, d)
        return (turnin)

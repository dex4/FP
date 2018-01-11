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

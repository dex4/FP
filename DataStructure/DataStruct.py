import sys
sys.path.append('../')
from Repositories.studentRepo import *
from Domain.student import *

s1 = Student(12, "Darjan", "912")
s2 = Student(13, "Andrei", "912")
s3 = Student(14, "Rad", "922")

def compareAlphaS(a, b):
    aN = a.getName()
    bN = b.getName()
    return (aN > bN) - (aN < bN)

def compareAID(a, b):
    i1 = a.getID()
    i2 = b.getID()
    return (i1 > i2) - (i1 < i2)

class DataStruct:
    def __init__(self):
        self.list = []
    def __iter__(self):
        return iter(self.list)
    def gnomeSort(self, theList, comp):
        pos = 0
        while(pos < len(theList)):
            if(pos == 0 or (comp(theList[pos], theList[pos-1]) == -1) or (comp(theList[pos], theList[pos-1]) == 0)):
                pos += 1
            else:
                aux = theList[pos]
                theList[pos] = theList[pos-1]
                theList[pos-1] = aux
                pos -= 1
        return theList
    def append(self, item):
        self.list.append(item)

sList = DataStruct()
sList.append(s1)
sList.append(s2)
sList.append(s3)
sList.list = sList.gnomeSort(sList.list, compareAlphaS)
"""
for c in sList:
    print(c)
"""
#comp(theList[pos], theList[pos-1]) == -1
#theList[pos].getName() >= theList[pos-1].getName()

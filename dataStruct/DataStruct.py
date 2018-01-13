import sys
sys.path.append('../')


def compareAlphaS(a, b):
    aN = a.getName()
    bN = b.getName()
    return (aN > bN) - (aN < bN)

def comp(a, b):
    return (a > b) - (a < b)

def filterByGroup(student, group):
    if(student.getGroup() != group):
        return False
    return True

def compareAID(a, b):
    i1 = a.getID()
    i2 = b.getID()
    return (i1 > i2) - (i1 < i2)

class DataStruct:
    def __init__(self):
        self.list = []
    def __len__(self):
        return len(self.list)
    def __iter__(self):
        self.count = 0
        return self
    def __next__(self):
        if self.count == len(self.list):
            raise StopIteration
        self.count += 1
        return self.count - 1
    def __getitem__(self,index):
        return self.list[index]
    def __setitem__(self,index,value):
        self.list[index] = value
    def __delitem__(self, index):
        del self.list[index]
    def gnomeSort(self, theList, comp):
        pos = 0
        while(pos < len(theList)):
            if(pos == 0 or (comp(theList[pos], theList[pos-1]) == 1) or (comp(theList[pos], theList[pos-1]) == 0)):
                pos += 1
            else:
                aux = theList[pos]
                theList[pos] = theList[pos-1]
                theList[pos-1] = aux
                pos -= 1
        return theList
    def filterFunc(self, group, fltr):
        newList = []
        for student in self.getList():
            if(fltr(student, group) == True):
                newList.append(student)
        return newList
    def getList(self):
        return self.list
    def append(self, item):
        self.list.append(item)
#comp(theList[pos], theList[pos-1]) == -1
#theList[pos].getName() >= theList[pos-1].getName()

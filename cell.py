class Cell:
    '''Represents a single cell on a Sudoku Board'''
    def __init__(self):
        self._num = None
        self.sections = []
        self.triedNums = set()
        self.locked = False
        self._maxNum = 9
    
    def getNum(self):
        '''Gets number currently contained in the cell'''
        return self._num

    def setNum(self, num):
        '''Sets _num if num is a legal entry in sudoku logic'''
        for section in self.sections:
            if num in section.nums():
                raise ValueError('Number already exists in section.')
        self.triedNums.add(num)
        self._num = num
    
    def getMaxNum(self):
        return self._maxNum

    def setMaxNum(self, maxNum):
        self._maxNum = maxNum

    def addSection(self, section):
        '''Adds a section that the cell belongs to.'''
        self.sections.append(section)

    def tryNextNum(self):
        '''Finds and returns the next legal digit not in triedNums'''
        if self.locked:
            return False
        takenNumbers = self.triedNums
        for section in self.sections:
            takenNumbers.update(section.nums())
        for num in range(1,self._maxNum+1):
            if num not in takenNumbers:
                return num
        return False

    def lock(self):
        '''Locks the cell so that the solver can't change its value'''
        self.locked = True

    def unlock(self):
        '''Unlocks the cell, allowing the solver to edit it'''
        self.locked = False
    
    def isLocked(self):
        '''Checks if the cell is locked'''
        return self.locked
    
    def resetTriedNums(self):
        '''Clears previously attempted numbers and the current value'''
        self.triedNums = set()
        self._num = None

    num = property(getNum, setNum)
    maxNum = property(getMaxNum, setMaxNum)

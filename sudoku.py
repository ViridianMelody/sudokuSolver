#!/usr/bin/env python3







class Sudoku:
    def __init__(self,size=3):
        self.size = size**2
        self.cells = {}
        self.boxes = [Section() for i in range(size**2)]
        self.rows = [Section() for i in range(size**2)]
        self.cols = [Section() for i in range(size**2)]
        for r in range(size**2):
            for c in range(size**2):
                newCell = Cell()
                self.rows[r].addCell(newCell)
                self.cols[c].addCell(newCell)
                boxIndex = (r//size)*size + (c//size)
                self.boxes[boxIndex].addCell(newCell)
                self.cells[(r,c)] = newCell

    def importPuzzle(self,board):
        for i, space in enumerate(board):
            if space != 0:
                row = i//self.size
                col = i%self.size
                self.setGivenCell(row,col,space)

    def setGivenCell(self, row, col, num):
        cell = self.cells[(row,col)]
        cell.num = num
        cell.lock()


    def solve(self):
        i = 0
        while i < self.size**2:
            if i < 0:
                return False
            row = i//self.size
            col = i%self.size
            currentCell = self.cells[(row,col)]
            if not currentCell.isLocked():
                backtracking = False
                nextNum = currentCell.findNext(self.size)
                if nextNum:
                    currentCell.setNum(nextNum)
                    i += 1
                else:
                    currentCell.resetTriedNums()
                    i -= 1
                    backtracking = True
            elif backtracking:
                i-=1
            else:
                i+=1
        return True

    def printResult(self):
        for row in self.rows:
            rowNums = []
            for cell in row.cells:
                rowNums.append(cell.num)
            print(rowNums)
            





class Section:
    def __init__(self):
        self.cells = []
    
    def addCell(self, cell):
        if cell.num in self.nums():
            raise ValueError('Number already exists in section.')
        self.cells.append(cell)
        cell.addSection(self)

    def nums(self):
        result = set()
        for cell in self.cells:
            if cell.num is not None:
                result.add(cell.num)
        return result





class Cell:
    def __init__(self):
        self._num = None
        self.sections = []
        self.triedNums = set()
        self.locked = False
    
    def getNum(self):
        return self._num

    def setNum(self, num):
        for section in self.sections:
            if num in section.nums():
                raise ValueError('Number already exists in section.')
        self.triedNums.add(num)
        self._num = num
    
    def addSection(self, section):
        self.sections.append(section)

    def findNext(self, maxNum):
        takenNumbers = self.triedNums
        for section in self.sections:
            takenNumbers.update(section.nums())
        for num in range(1,maxNum+1):
            if num not in takenNumbers:
                return num
        return False

    def lock(self):
        self.locked = True

    def unlock(self):
        self.locked = False
    
    def isLocked(self):
        return self.locked
    
    def resetTriedNums(self):
        self.triedNums = set()
        self._num = None

    num = property(getNum, setNum)







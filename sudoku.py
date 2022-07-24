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

    def setGivenCell(self, row, col, num):
        self.cells[(row,col)].num = num

    def solve(self):
        
        pass


class Section:
    def __init__(self):
        self.cells = []
    
    def addCell(self, cell):
        if cell.num in self.nums():
            raise ValueError('Number already exists in section.')
        self.cells.append(cell)
        cell.addSection(self)

    def nums(self):
        result = []
        for cell in self.cells:
            if cell.num is not None:
                result.append(cell.num)





class Cell:
    def __init__(self):
        self.num = None
        self.sections = []
        self.possibleNums = []
    
    def getNum(self):
        return self._num

    def setNum(self, num):
        self._num = num
    
    def addSection(self, section):
        self.sections.append(section)
    
    def findPossibleNums(self):
        for section in self.sections:



    num = property(getNum, setNum)

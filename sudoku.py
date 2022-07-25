#!/usr/bin/env python3

from cell import Cell
from section import Section

'''Sudoku solver using backtracking'''

class Sudoku:
    def __init__(self,size=9, puzzle=None):
        '''
        Sudoku board constructor.
        If puzzle is defined, it will generate filled board
        If size is defined, it will generate an empty board of given size
        puzzle: list[int]; 0 represents empty space
        size: int; Default is 9, for a standard sudoku
        '''
        if puzzle is not None:
            self.importPuzzle(puzzle)
        else:
            self.size = size
            self.generateGrid()
        self.stepsTaken = 0

    def setSize(self, size):
        '''Changes the size of the board and calls generateGrid'''
        self.size = size
        self.generateGrid

    def generateGrid(self):
        '''
        Generates Cells and places them in corresponding Sections.
        self.size must be set before calling.
        Clears any existing puzzle.
        '''
        self.cells = []
        self.boxes = [Section() for i in range(self.size)]
        self.rows = [Section() for i in range(self.size)]
        self.cols = [Section() for i in range(self.size)]
        boxSize = int(self.size**0.5)
        for r in range(self.size):
            for c in range(self.size):
                newCell = Cell()
                self.rows[r].addCell(newCell)
                self.cols[c].addCell(newCell)
                boxIndex = (r//boxSize)*boxSize + (c//boxSize)
                self.boxes[boxIndex].addCell(newCell)
                self.cells.append(newCell)
        

    def importPuzzle(self,board):
        '''
        Generates grid and fills given spaces
        board must contain x**4 elements
        board: list[int]; 0 represents empty space
        '''
        self.size = int(len(board)**0.5)
        self.generateGrid()
        for i, space in enumerate(board):
            if space != 0:
                self.setGivenCell(i,space)

    def setGivenCell(self, i, num):
        '''
        Sets the value of a given cell and locks it
        i: int; index of cell to edit
        num: int; value to set cell to
        '''
        cell = self.cells[i]
        cell.num = num
        cell.lock()


    def solve(self):
        '''
        Searches for a solution to the puzzle
        Returns True if successful, false otherwise
        '''
        self.stepsTaken = 0
        try:
            i = 0
            while i < len(self.cells):
                self.stepsTaken += 1
                i = self.findNextUnlockedCell(i)
                cell = self.cells[i]
                num = cell.tryNextNum()
                if num:
                    cell.num = num
                    i += 1
                else:
                    i = self.backtrack(i)
            return True
        except:
            print('Solution not found')
            return False

    def findNextUnlockedCell(self, i):
        '''
        Finds the next unlocked cell, starting with cell at index i
        i: int; starting cell index
        '''
        while i < len(self.cells):
            currentCell = self.cells[i]
            if currentCell.isLocked():
                i += 1
            else:
                return i
        raise IndexError

    def backtrack(self, i):
        '''
        Backtracks to last unlocked cell that still has unused possible digits.
        Any cells that have no unused digits have their triedNums reset
        Once found, sets the value to next available digit, and returns index of next cell.
        i: int; starting cell index
        '''
        while i >= 0:
            currentCell = self.cells[i]
            if currentCell.isLocked():
                i -= 1
                continue
            num = currentCell.tryNextNum()
            if num:
                currentCell.num = num
                return i + 1
            else:
                currentCell.resetTriedNums()
                i -= 1
        raise IndexError

    def __repr__(self):
        result = f'Steps taken: {self.stepsTaken}\n'
        for row in self.rows:
            for cell in row.cells:
                if cell.num is None:
                    result += '|-'
                else:
                    result += f'|{cell.num}'
            result += '|\n'
        return result
            



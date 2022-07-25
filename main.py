#!/usr/bin/env python3
from tkinter.filedialog import askopenfile, asksaveasfile
from os import getcwd
from sudoku import Sudoku



def main():
    '''Driver for Sudoku solver'''
    cwd = getcwd()
    inputFile = askopenfile(mode='r', initialdir=cwd, title='Open Sudoku file')
    puzzle = parseSudokuInput(inputFile)
    sudoku = Sudoku(puzzle = puzzle)
    output = 'Imported puzzle:\n'
    output += str(sudoku)
    sudoku.solve()
    output += 'Solved puzzle:\n'
    output += str(sudoku)
    outputFile = asksaveasfile(mode='w+', initialdir=cwd, title='Save solution as')
    outputFile.write(output)
    
     

def parseSudokuInput(inputFile):
    result = []
    line = inputFile.readline().strip()
    while line:
        for char in line.split(','):
            result.append(int(char))
        line = inputFile.readline()
    return result



if __name__ == '__main__':
    main()
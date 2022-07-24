#!/usr/bin/env python3
from sudoku import Sudoku



def main():
    easyPuzzle = [
        0,0,5,3,6,0,4,0,0,
        9,6,2,0,0,4,0,7,0,
        3,0,4,0,2,9,0,6,0,
        8,2,0,9,4,0,0,1,3,
        0,4,9,0,3,0,0,5,7,
        0,0,0,2,0,0,9,8,0,
        4,0,6,0,0,1,0,0,2,
        0,0,0,6,9,3,0,0,5,
        0,0,3,0,8,0,0,0,0
    ]
    hardPuzzle = [
        0,0,7,0,0,0,0,0,3,
        0,0,9,0,6,0,0,0,0,
        3,6,0,0,0,8,2,0,0,
        0,0,6,0,0,0,0,0,0,
        5,1,0,0,8,0,0,0,9,
        0,0,0,0,0,2,0,4,0,
        0,0,0,5,0,0,9,0,0,
        8,3,0,0,1,0,0,0,5,
        7,0,0,0,0,0,0,0,0
    ]
    
    solvePuzzle(easyPuzzle)
    solvePuzzle(hardPuzzle)

def solvePuzzle(puzzle):
    sudoku = Sudoku(3)
    sudoku.importPuzzle(puzzle)
    if sudoku.solve():
        sudoku.printResult()
    else:
        print('failed')



if __name__ == '__main__':
    main()
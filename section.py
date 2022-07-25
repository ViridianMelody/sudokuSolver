
class Section:
    '''
    A collection of Cells that must have unique values
    Can represent a row, column, or box.
    '''
    def __init__(self):
        self.cells = []
    
    def addCell(self, cell):
        '''
        Adds a cell to the section if its value doesn't conflict with other cells
        '''
        if cell.num in self.nums():
            raise ValueError('Number already exists in section.')
        self.cells.append(cell)
        cell.addSection(self)

    def nums(self):
        '''
        Returns a set of numbers contained in member Cells.
        '''
        result = set()
        for cell in self.cells:
            if cell.num != None:
                result.add(cell.num)
        return result
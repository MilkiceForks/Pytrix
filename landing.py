class Matrix:
    row = 0
    column = 0
    core = []

    def init(self):
        print('Please define this matrix. End with a "."')
        while True:
            raw = input().split()
            if raw[0] == '.':
                break
            if self.column == 0:
                self.column = len(raw)
            if self.column != len(raw):
                print('Error: number of element in a single column.\nOperation Terminated.')
                break
            self.core.append([int(i) for i in raw])
            self.row += 1

    def __add__(self, other):
        if Matrix.errorAdd(self.row, self.column, other.row, other.column):
            return None
        output = Matrix()
        for i in range(self.row):
            for j in range(self.column):
                output.core[i][j] = self.core[i][j] + other.core[i][j]
        return output

    @classmethod
    def errorAdd(cls, selfRow, selfColumn, otherRow, otherColumn) -> bool:
        condition = False
        if selfRow != otherRow:
            print('Error: The row value of two matrix are not the same.')
            condition = True
        if selfColumn != otherColumn:
            print('Error: The column value of two matrix are not the same.')
            condition = True
        return condition


A = Matrix()
A.init()
B = Matrix()
B.init()
print((A + B).core, A.row, A.column)  # Cautious: NoneType value could be returned by (A + B)

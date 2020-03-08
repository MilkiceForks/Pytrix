class Matrix:
    def __init__(self):
        self._row = 0
        self._column = 0
        self._core = []

    @property
    def core(self):
        # return a shallow copy, prevent external manipulation
        return self._core.copy()

    @property
    def row(self):
        return self._row

    @property
    def column(self):
        return self._column

    def init(self):
        print('Please define this matrix. End with a "."')
        while True:
            raw = input().split()
            if raw[0] == '.':  # the symbol that stop input
                break
            if self._column == 0:
                self._column = len(raw)
            if self._column != len(raw):
                print('Error: number of element in a single column.\nOperation Terminated.')
                break
            self._core.append([int(i) for i in raw])
            self._row += 1

    def __add__(self, other):
        if Matrix.errorAdd(self._row, self._column, other.row, other.column):
            return None
        output = Matrix()
        output._row, output._column = self._row, self._column
        for i in range(self._row):
            tmpRow = []
            for j in range(self._column):
                tmpRow.append(self._core[i][j] + other.core[i][j])
            output._core.append(tmpRow)
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
print((A + B).core, A.row, A.column)  # Caution: NoneType value could be returned by (A + B)

from calculation.error import *


class Matrix:
    def __init__(self, row=0, column=0):
        self._row = row
        self._column = column
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
        print('Please define this calculation. End with a "."')
        while True:
            raw = input().split()
            if raw[0] == '.':  # the symbol that stop input
                break
            if self._column == 0:
                self._column = len(raw)
            if self._column != len(raw):
                raise MatrixElementAmountError(self._column)
            try:
                self._core.append([int(i) for i in raw])
            except ValueError as error:
                raise MatrixInputError(error)
            self._row += 1

    def __add__(self, other):
        if self._row != other.row or self._column != other.column:
            raise MatrixAdditionError(self._row != other.row, self._column != other.column)
        output = Matrix(self._row, self._column)
        for i in range(self._row):
            tmpRow = []
            for j in range(self._column):
                tmpRow.append(self._core[i][j] + other.core[i][j])
            output._core.append(tmpRow)
        return output


'''
A = Matrix()
try:
    A.init()
except MatrixInputError as error:
    print(error)
except MatrixElementAmountError as error:
    print(error)

B = Matrix()
try:
    B.init()
except MatrixInputError as error:
    print(error)
except MatrixElementAmountError as error:
    print(error)

try:
    print((A + B).core, A.row, A.column)
except AttributeError as error:
    print(error)
except MatrixAdditionError as error:
    print(error)
'''

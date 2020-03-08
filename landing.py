from matrix.core import Matrix
from matrix.error import *

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

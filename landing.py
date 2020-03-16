from interaction.control import Control, command

while True:
    print('>>> ', end='')
    line = input().split()
    if len(line):
        if line[0] in command['quit']:
            Control.exit(0)
        # TODO elif line[0] in command['declare']:
        # TODO elif line[0] in command['define']:
        # TODO elif line[0] in command['variable']:
        # TODO elif line[0] in command['remove']:
        # TODO elif line[0] in command['list']:
        else:
            print('Operation not found.')

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

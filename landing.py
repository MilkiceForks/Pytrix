from interaction.control import Control, command

while True:
    line = input('>>> ').split()
    length = len(line)
    if length == 0:
        pass
    elif length == 1:
        if line[0] in command['quit']:
            Control.exit(0)
            break                              # note that this line is unreachable
        elif line[0] in command['list']:
            Control.list()
    elif length == 2:
        if line[0] in command['declare']:
            Control.declare()
        elif line[0] in command['define']:
            Control.define()
        elif line[0] in command['remove']:
            Control.remove()
    elif length >= 3:
        if line[0] in command['add']:
            Control.add()
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

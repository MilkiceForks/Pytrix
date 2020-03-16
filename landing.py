from interaction.control import Control

while True:
    print('>>> ', end='')
    line = input().split()
    if len(line) != 0:
        if line[0] in ['end', 'quit', 'exit', 'esc', 'escape']:
            Control.exit(0)
        # TODO elif line[0] in ['dec', 'declare']:
        # TODO elif line[0] in ['def', 'define']:
        # TODO elif line[0] in ['var', 'variable']:
        # TODO elif line[0] in ['del', 'delete', 'rm', 'remove']:
        # TODO elif line[0] in ['lis', 'list', 'ls']:

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

from interaction.control import Control, commandDict, commandFunc
from memory.list import matrixList, init
from command.process import OptionsParser

init()

while True:
    line = input('>>> ').split()
    length = len(line)
    if length == 0:
        pass
    else:
        if line[0] not in commandFunc:
            print('Error: Unknown command "%s"' % line[0])
        else:
            op = OptionsParser(line[0], line[1:])
            status, message, argsConfig, values = op.parse()
            if not status:
                print(message)
            else:
                func = getattr(Control, commandFunc[line[0]])
                func(line[0], argsConfig, values)
        '''
        if line[0] in commandDict['exit']:
            Control.exit(line[0], line[1:])
        elif line[0] in commandDict['list']:
            Control.list()
        elif line[0] in commandDict['declare']:
            Control.declare()
        elif line[0] in commandDict['define']:
            Control.define()
        elif line[0] in commandDict['remove']:
            Control.remove()
        elif line[0] in commandDict['add']:
            Control.add()
        else:
            print('Error: Unknown command "%s"' % line[0])
        '''

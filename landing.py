from interaction.control import Control, command

while True:
    line = input('>>> ').split()
    length = len(line)
    if length == 0:
        pass
    else:
        if line[0] in command['exit']:
            Control.exit(line[0], line[1:])
        elif line[0] in command['list']:
            Control.list()
        elif line[0] in command['declare']:
            Control.declare()
        elif line[0] in command['define']:
            Control.define()
        elif line[0] in command['remove']:
            Control.remove()
        elif line[0] in command['add']:
            Control.add()
        else:
            print('Error: Unknown command "%s"' % line[0])

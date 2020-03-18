from calculation.core import Matrix
from memory.list import matrixList

commandDict = {'exit': ['end', 'quit', 'exit', 'esc', 'escape'],
               'list': ['lis', 'list', 'ls'],
               'declare': ['dec', 'declare'],
               'define': ['def', 'define'],
               'remove': ['del', 'delete', 'rm', 'remove'],
               'add': ['add']
               }


class Control:
    @classmethod
    def exit(cls, command, options):
        optionDict = {'-f': False}
        for key in list(optionDict.keys()):
            if options.count(key):
                optionDict[key] = True
                for i in range(options.count(key)):
                    options.remove(key)
        if len(options) != 0:
            print('Error: Unknown option in command "%s":' % command, end=' ')
            for i in options:
                print(i, end=' ')
            print('')
        else:
            if optionDict.get('-f'):
                exit(0)
            else:
                response = input('Are you sure you want to quit? (y/n) ')
                if response in ['y', 'Y']:
                    exit(0)
                elif response in ['n', 'N']:
                    pass
                else:
                    print('Unknown command: ' + response)
        return None

    @classmethod
    def list(cls):
        for i in range(len(matrixList)):
            print(matrixList[i].name + ': ' + str(matrixList[i].core))

    @classmethod
    def declare(cls):
        pass  # TODO: Define this function

    @classmethod
    def define(cls):
        pass  # TODO: Define this function

    @classmethod
    def remove(cls):
        pass  # TODO: Define this function

    @classmethod
    def add(cls):
        pass  # TODO: Define this function

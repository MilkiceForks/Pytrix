from calculation.core import Matrix

command = {'exit': ['end', 'quit', 'exit', 'esc', 'escape'],
           'list': ['lis', 'list', 'ls'],
           'declare': ['dec', 'declare'],
           'define': ['def', 'define'],
           'remove': ['del', 'delete', 'rm', 'remove'],
           'add': ['add']
           }


class Control:
    @classmethod
    def exit(cls, original, detail):
        optionDisc = {'-f': False}
        for option in list(optionDisc.keys()):
            if detail.count(option):
                optionDisc[option] = True
                for i in range(len(detail)):
                    if detail[i] == option:
                        del detail[i]
        if len(detail) != 0:
            print('Error: Unknown option in command "%s":' % original, end=' ')
            for i in detail:
                print(i, end=' ')
            print('')
        else:
            if optionDisc.get('-f'):
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
        pass  # TODO: Define this function

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

from calculation.core import Matrix

command = {'quit': ['end', 'quit', 'exit', 'esc', 'escape'],
           'declare': ['dec', 'declare'],
           'define': ['def', 'define'],
           'variable': ['var', 'variable'],
           'remove': ['del', 'delete', 'rm', 'remove'],
           'list': ['lis', 'list', 'ls']
           }


class Control:
    @classmethod
    def exit(cls, num):
        print('Are you sure you want to quit? (y/n) ', end='')
        response = input()
        if response in ['y', 'Y']:
            exit(num)
        return None

    @classmethod
    def add(cls):
        pass  # TODO: Define this function, Σ.

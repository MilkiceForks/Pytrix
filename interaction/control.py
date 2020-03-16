from calculation.core import Matrix

command = {'quit': ['end', 'quit', 'exit', 'esc', 'escape'],
           'list': ['lis', 'list', 'ls'],
           'declare': ['dec', 'declare'],
           'define': ['def', 'define'],
           'remove': ['del', 'delete', 'rm', 'remove'],
           'add': ['add']
           }


class Control:
    @classmethod
    def exit(cls, num):
        response = input('Are you sure you want to quit? (y/n) ')
        if response in ['y', 'Y']:
            exit(num)
        elif response in ['n', 'N']:
            return None
        else:
            print('Invalid command!')
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

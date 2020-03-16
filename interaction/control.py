from calculation.matrix import Matrix


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

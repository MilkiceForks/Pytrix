class MatrixError(Exception):
    pass


class MatrixAdditionError(MatrixError):
    def __init__(self, flagA, flagB):
        self.__flagA = flagA
        self.__flagB = flagB

    def __str__(self):
        if self.__flagA:
            return 'The row value of two matrix are not the same.'
        if self.__flagB:
            return 'The column value of two matrix are not the same.'


class MatrixElementAmountError(MatrixError):
    def __init__(self, column):
        self.__column = str(column)

    def __str__(self):
        return 'The element amount of each row needs to be ' + self.__column


class MatrixInputError(MatrixError):
    def __init__(self, error):
        self.__error = str(error)

    def __str__(self):
        return self.__error

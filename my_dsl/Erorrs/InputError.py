class UserInputError(Exception):
    def __init__(self, message, ):
        super(UserInputError, self).__init__(message)


class InputFileNotFound(UserInputError):
    def __init__(self):
        super(InputFileNotFound, self).__init__(message="input file not found ")


class OutputFileNotFound(UserInputError):
    def __init__(self):
        super(OutputFileNotFound, self).__init__(message="output file not found ")

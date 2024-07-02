class UserInputError(Exception):
    def __init__(self, message, ):
        super(UserInputError, self).__init__(message)


class ExportFileError(UserInputError):
    def __init__(self, var):
        super(ExportFileError, self).__init__(message=f"variable {var} not declared !!!")

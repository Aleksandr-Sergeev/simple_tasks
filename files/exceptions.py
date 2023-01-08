

class FileManagementException(Exception):

    def __init__(self, source: str, message: str | None = None):
        self.source = source
        self.message = message
        super().__init__(self.message)

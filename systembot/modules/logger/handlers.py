import logging


class StreamHandler(logging.StreamHandler):
    def __init__(self, formatter=None):
        super().__init__()
        if isinstance(formatter, type(None)):
            raise TypeError('Logger formatter cannot be of type None')
        self.setFormatter(formatter)

class FileHandler(logging.FileHandler):
    def __init__(self, path, formatter=None):
        super().__init__(filename=path)
        if isinstance(formatter, type(None)):
            raise TypeError('Logger formatter cannot be of type None')
        self.setFormatter(formatter)

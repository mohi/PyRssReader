from inputter.fileinputreader import FileInputReader
from inputter.urlinputreader import UrlInputReader

class InputReaderFactory:
    """
    """
    @staticmethod
    def createInputReader(input_src, input_type):
        if input_type=='url':
            return UrlInputReader(input_src)
        elif input_type=='file':
            return FileInputReader(input_src)
        else:
            raise


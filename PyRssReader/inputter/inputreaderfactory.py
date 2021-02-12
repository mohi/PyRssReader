from inputter.fileinputreader import FileInputReader
from inputter.urlinputreader import UrlInputReader
from inputter.inputtype import InputType

class InputReaderFactory:
    """
    """
    @staticmethod
    def createInputReader(input_type, input_src):
        if input_type== InputType.URL:
            return UrlInputReader(input_src)
        elif input_type== InputType.FILE:
            return FileInputReader(input_src)
        else:
            raise


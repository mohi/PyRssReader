from PyRssReader.inputter.fileinputreader import FileInputReader
from PyRssReader.inputter.urlinputreader import UrlInputReader
from PyRssReader.inputter.inputtype import InputType

class InputReaderFactory:
    """
    Implements factory module for selection of
    inputreaders based on input arguments
    """

    @staticmethod
    def createInputReader(input_type, input_src):
        if input_type== InputType.URL:
            return UrlInputReader(input_src)
        elif input_type== InputType.FILE:
            return FileInputReader(input_src)
        else:
            raise


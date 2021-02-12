from inputter.inputreaderinterface import InputReaderInterface

class FileInputReader(InputReaderInterface):
    """
    Read text from file
    """
    def __init__(self, input_src):
        self.__src_file = input_src

    def read(self):
        with open(self.__src_file, 'r') as f:
            data = f.read()
        return data

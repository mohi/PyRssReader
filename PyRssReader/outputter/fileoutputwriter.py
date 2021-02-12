from outputter.outputwriterinterface import OutputWriterInterface

class FileOutputWriter(OutputWriterInterface):
    """
    Write text to output file
    """
    def __init__(self, output_src):
        self.__output_file = output_src

    def write(self, content):
        with open(self.__output_file, 'w') as f:
            f.write(content)
        return True


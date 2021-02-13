from PyRssReader.outputter.outputwriterinterface import OutputWriterInterface


class FileOutputWriter(OutputWriterInterface):
    """
    Implements module for Write text to
    output file on the disk
    """
    def __init__(self, output_src):
        self.__output_file = output_src

    def write(self, content):
        with open(self.__output_file, 'w') as f:
            f.write(content)
        return True

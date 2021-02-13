from PyRssReader.outputter.fileoutputwriter import FileOutputWriter
from PyRssReader.outputter.stdoutputwriter import StdOutputWriter
from PyRssReader.outputter.outputtype import OutputType

class OutputWriterFactory:
    """
    Implments factory module for selection
    of output writing method
    """

    @staticmethod
    def createOutputWriter(output_type, output_src):
        if output_type==OutputType.FILE:
            return FileOutputWriter(output_src)
        elif output_type==OutputType.STDOUT:
            return StdOutputWriter()
        else:
            raise

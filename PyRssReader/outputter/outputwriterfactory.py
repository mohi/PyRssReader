from outputter.fileoutputwriter import FileOutputWriter
from outputter.stdoutputwriter import StdOutputWriter
from outputter.outputtype import OutputType

class OutputWriterFactory:
    """
    """
    @staticmethod
    def createOutputWriter(output_type, output_src):
        if output_type==OutputType.FILE:
            return FileOutputWriter(output_src)
        elif output_type==OutputType.STDOUT:
            return StdOutputWriter()
        else:
            raise

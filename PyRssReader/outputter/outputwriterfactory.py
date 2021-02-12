from outputter.fileoutputwriter import FileOutputWriter
from outputter.stdoutputwriter import StdOutputWriter

class OutputWriterFactory:
    """
    """
    @staticmethod
    def createOutputWriter(output_src, output_type):
        if output_type=='file':
            return FileOutputWriter(output_src)
        elif output_type=='stdout':
            return StdOutputWriter()
        else:
            raise



from outputter.outputwriterinterface import OutputWriterInterface

class StdOutputWriter(OutputWriterInterface):
    """
    Write text to std out
    """
    def __init__(self):
        pass

    def write(self, content):
        import sys
        sys.stdout.write(content)
        return True


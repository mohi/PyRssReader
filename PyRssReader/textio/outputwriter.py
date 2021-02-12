import abc

class OutputWriterInterface(metaclass=abc.ABCMeta):
    """
    Base class to write outputs
    """
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'write') and
                callable(subclass.write) or
                NotImplemented)

    @abc.abstractmethod
    def write(self):
        """Write text to destination"""
        raise NotImplementedError

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

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


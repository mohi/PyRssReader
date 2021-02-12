import abc

class InputReaderInterface(metaclass=abc.ABCMeta):
    """
    Base class to read inputs
    """
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'read') and
                callable(subclass.read) or
                NotImplemented)

    @abc.abstractmethod
    def read(self):
        """Read text from src"""
        raise NotImplementedError


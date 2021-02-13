import abc

class InputReaderInterface(metaclass=abc.ABCMeta):
    """
    Defines interface of text input readers
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


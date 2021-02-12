import abc

class ConverterInterface(metaclass=abc.ABCMeta):
    """
    Base class to convert text
    """
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'process') and
                callable(subclass.process) or
                NotImplemented)

    @abc.abstractmethod
    def process(self, text: str):
        """process text from input"""
        raise NotImplementedError



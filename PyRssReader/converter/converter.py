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


class CutConverter(ConverterInterface):
    """
    """
    def __init__(self):
        pass

    def process(self, text: str) -> str:
        # iterate through the text
        # trim title and body to 10
        return text

class ReplaceConverter(ConverterInterface):
    """
    """
    def __init__(self, regex_form):
        self.__regex_form = regex_form

    def process(self, text: str) -> str:
        # apply regex formula and return text
        return text


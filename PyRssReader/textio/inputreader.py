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

class UrlInputReader(InputReaderInterface):
    """
    Read text from Rss feed Url
    """
    def __init__(self, input_src):
        self.__src_url = input_src
        self.__process_url()

    def __process_url(self):
        self.__src_url = self.__src_url + 'feed/'

    def read(self):
        import requests
        response = requests.get(self.__src_url)
        data = response.text
        return data

class FileInputReader(InputReaderInterface):
    """
    Read text from file
    """
    def __init__(self, input_src):
        self.__src_file = input_src

    def read(self):
        with open(self.__src_file, 'r') as f:
            data = f.read()
        return data


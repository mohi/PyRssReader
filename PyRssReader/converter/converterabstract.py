import abc
import xml.etree.ElementTree as ET
from io import StringIO


class ConverterAbstract(metaclass=abc.ABCMeta):
    """
    Abstract base class to convert text. Also provides
    basic methods for xml processing.
    """
    @classmethod
    def __subclasshook__(cls, subclass):
        return ((hasattr(subclass, 'process') and callable(subclass.process))
                or NotImplemented)

    @abc.abstractmethod
    def process(self, text: str):
        """process text from input"""
        raise NotImplementedError

    def _textToXml(self, text):
        # preserve xml namespaces
        # find namespaces
        namespaces = dict([node for _, node in ET.iterparse(StringIO(text), \
                                                            events=['start-ns']) \
                          ])
        for ns in namespaces:
            # register namespaces into the elementtree
            ET.register_namespace(ns, namespaces[ns])

        self.__xmltree = ET.fromstring(text)
        return self.__xmltree

    def _xmlToText(self):
        __out_txt = ET.tostring(self.__xmltree, encoding='utf8').decode()
        return __out_txt

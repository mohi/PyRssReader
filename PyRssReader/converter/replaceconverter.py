from PyRssReader.converter.converterabstract import ConverterAbstract
import re


class ReplaceConverter(ConverterAbstract):
    """
    Implements data processor which replaces
    text using the pattern inside the textual
    tags- title, subtitle, author, summary, content
    """
    def __init__(self, regex_form):
        self.__regex_form = regex_form

    def process(self, text: str) -> str:
        # create xmltree from text
        __xmltree = self._textToXml(text)

        __regex_find, __regex_replace = self.__regex_form.split('/')

        # for every tag inside xmltree
        for elem in __xmltree.iter():
            # if tag of element is of title and summary
            if (elem.tag.split('}')[-1]
                    in ['title', 'subtitle', 'author', 'summary', 'content']):
                elem.text = re.sub(__regex_find, __regex_replace, elem.text)

        # create text back from xmltree
        return self._xmlToText()

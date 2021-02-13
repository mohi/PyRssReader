from PyRssReader.converter.converterabstract import ConverterAbstract


class CutConverter(ConverterAbstract):
    """
    Implements text processor which trims
    all title and summary inside xml
    document to length 10
    """

    TRIM_LEN = 10

    def __init__(self):
        pass

    def process(self, text: str) -> str:
        # create xmltree from text
        __xmltree = self.textToXml(text)

        # for every tag inside xmltree
        for elem in __xmltree.iter():
            # if tag of element is of title and summary
            if (elem.tag.split('}')[-1] in ['title', 'summary']):
                elem.text = elem.text[0:self.TRIM_LEN]

        # create text back from xmltree
        return self.xmlToText()

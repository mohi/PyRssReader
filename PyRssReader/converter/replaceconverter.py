from converter.converterinterface import ConverterInterface

class ReplaceConverter(ConverterInterface):
    """
    """
    def __init__(self, regex_form):
        self.__regex_form = regex_form

    def process(self, text: str) -> str:
        # apply regex formula and return text
        return text



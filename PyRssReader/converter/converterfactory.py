from PyRssReader.converter.cutconverter import CutConverter
from PyRssReader.converter.replaceconverter import ReplaceConverter
from PyRssReader.converter.convertertype import ConverterType

class ConverterFactory:
    """
    Implements factory for creating converters
    as per the pipeline requirement
    """

    @staticmethod
    def createConverter(converter_type, converter_arg):
        if (converter_type == ConverterType.CUT):
            return CutConverter()
        elif (converter_type == ConverterType.REPLACE):
            return ReplaceConverter(converter_arg)
        else:
            raise


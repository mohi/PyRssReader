from converter.cutconverter import CutConverter
from converter.replaceconverter import ReplaceConverter
from converter.convertertype import ConverterType

class ConverterFactory:
    """
    """
    @staticmethod
    def createConverter(converter_type, converter_arg):
        if (converter_type == ConverterType.CUT):
            return CutConverter()
        elif (converter_type == ConverterType.REPLACE):
            return ReplaceConverter(converter_arg)
        else:
            raise


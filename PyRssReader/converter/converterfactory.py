from converter.cutconverter import CutConverter
from converter.replaceconverter import ReplaceConverter

class ConverterFactory:
    """
    """
    @staticmethod
    def createConverter(converter_info):
        if ('cut' == converter_info):
            return CutConverter()
        elif converter_info.startswith('replace'):
            return ReplaceConverter(converter_info[8:-1])
        else:
            raise


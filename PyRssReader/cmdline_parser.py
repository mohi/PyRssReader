import argparse
from PyRssReader.inputter.inputtype import InputType
from PyRssReader.converter.convertertype import ConverterType
from PyRssReader.outputter.outputtype import OutputType
from collections import namedtuple

class CmdlineParser(argparse.ArgumentParser):
    """
    Implements parser to fetch user command line
    inputs and infer them
    """

    @staticmethod
    def inferConvert(converter_text):
        __ConvertInfo = namedtuple('converterinfo', ['type', 'arg'])
        converter_text = converter_text.strip()
        if ('cut' == converter_text):
            return __ConvertInfo(ConverterType.CUT, None)
        elif converter_text.startswith('replace'):
            return __ConvertInfo(ConverterType.REPLACE, converter_text[9:-2])
        else:
            raise

    def __inferConverter(self):
        if self.__args.convert:
            converters_info = self.__args.convert.split(',')
            self.__args.num_converter = len(converters_info)
            self.__args.convert_info = [CmdlineParser.inferConvert(txt) for txt in converters_info]
        else:
            raise

    def __inferInput(self):
        self.__InputInfo = namedtuple('InputInfo', ['type', 'src'])
        if self.__args.input:
            if self.__args.input.endswith('.txt'):
                self.__args.input_info = self.__InputInfo(InputType.FILE, self.__args.input)
            else:
                self.__args.input_info = self.__InputInfo(InputType.URL, self.__args.input)
        else:
            raise

    def __inferOutput(self):
        self.__OutputInfo = namedtuple('OutputInfo', ['type', 'src'])
        if self.__args.output and self.__args.output.endswith('.txt'):
            self.__args.output_info = self.__OutputInfo(OutputType.FILE, self.__args.output)
        else:
            self.__args.output_info = self.__OutputInfo(OutputType.STDOUT, None)

    def parse_args(self):
        self.__args = super(CmdlineParser, self).parse_args()
        self.__inferInput()
        self.__inferOutput()
        self.__inferConverter()
        return self.__args

class CmdlineParserBuilder():
    """
    Implements builder for creating
    command line parser
    """
    def __init__(self):
        pass

    def build(self):
        self.cmd_parser = CmdlineParser()
        self.cmd_parser.add_argument("--input", "-i", \
                         help="input url or file path")
        self.cmd_parser.add_argument("--convert", "-c", \
                         help="functions to apply on input")
        self.cmd_parser.add_argument("--output", "-o", \
                         help="output path")
        return self.cmd_parser

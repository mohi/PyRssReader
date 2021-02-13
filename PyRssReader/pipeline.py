from PyRssReader.inputter.inputreaderfactory import InputReaderFactory
from PyRssReader.converter.converterfactory import ConverterFactory
from PyRssReader.outputter.outputwriterfactory import OutputWriterFactory


class Pipeline:
    """
    Implments pipeline for fetching input and
    applying converter and then outputting
    """
    def __init__(self):
        pass

    def setInputReader(self, input_info):
        self.__input_reader = InputReaderFactory.createInputReader(
            input_info.type, input_info.src)

    def setOutputWriter(self, output_info):
        self.__output_reader = OutputWriterFactory.createOutputWriter(
            output_info.type, output_info.src)

    def setConverters(self, convert_info):
        self.__num_converts = len(convert_info)
        self.__first_converter = ConverterFactory.createConverter(
            convert_info[0].type, convert_info[0].arg)
        if self.__num_converts > 1:
            self.__second_converter = ConverterFactory.createConverter(
                convert_info[1].type, convert_info[1].arg)

    def run(self):
        content = self.__input_reader.read()
        content = self.__first_converter.process(content)
        if self.__num_converts > 1:
            content = self.__second_converter.process(content)
        self.__output_reader.write(content)

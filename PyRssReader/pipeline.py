from converter.converterfactory import ConverterFactory
from textio.inputreaderfactory import InputReaderFactory
from textio.outputwriterfactory import OutputWriterFactory

class Pipeline:
    """
    Pipeline for taking input and applying converter and then outputting
    """
    def __init__(self):
        pass

    def __repr__(self):
        pass

    def setInputSource(self, input_src, input_type):
        self.__input_src = InputReaderFactory.createInputReader(input_src, input_type)

    def setOutputDestination(self, output_src, output_type):
        self.__output_src = OutputWriterFactory.createOutputWriter(output_src, output_type)

    def setConverters(self, converters):
        self.__converters = []
        for converter in converters:
            self.__converters.append(ConverterFactory.createConverter(converter))

    def run(self):
        content = self.__input_src.read()
        for converter in self.__converters:
            content = converter.process(content)
        self.__output_src.write(content)

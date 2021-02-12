import argparse

class CliParser(argparse.ArgumentParser):
    """
    """
    def infer_args(self):
        self.args = super(CliParser, self).parse_args()
        if self.args.input:
            if self.args.input.endswith('.txt'):
                self.args.input_src = self.args.input
                self.args.input_type = 'file'
            else:
                self.args.input_src = self.args.input
                self.args.input_type = 'url'
        else:
            raise

        if self.args.output:
            if self.args.output.endswith('.txt'):
                self.args.output_src = self.args.output
                self.args.output_type = 'file'
            else:
                self.args.output_src = None
                self.args.output_type = 'stdout'
        else:
            self.args.output_src = None
            self.args.output_type = 'stdout'

        if self.args.convert:
            self.args.convert = self.args.convert.split(',')
        return self.args



class CliParserBuilder():
    """
    """
    def __init__(self):
        pass

    def build(self):
        self.CliParser = CliParser()
        self.CliParser.add_argument("--input", "-i", \
                         help="input url or file path")
        self.CliParser.add_argument("--convert", "-c", \
                         help="functions to apply on input")
        self.CliParser.add_argument("--output", "-o", \
                         help="output path")
        return self.CliParser

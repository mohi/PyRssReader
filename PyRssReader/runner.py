from PyRssReader.cmdline_parser import CmdlineParserBuilder
from PyRssReader.pipeline import Pipeline

class Runner:
    """
    Implements a job running module which
    takes user input and executes the pipeline
    accordingly.
    """

    def __init__(self):
        pass

    def runCmdline(self):
        cmdline_parser = CmdlineParserBuilder().build()
        args = cmdline_parser.parse_args()
        job_pipe = Pipeline()
        job_pipe.setInputReader(args.input_info)
        print(args.convert_info)
        job_pipe.setConverters(args.convert_info)
        job_pipe.setOutputWriter(args.output_info)
        print(job_pipe.__dict__)
        job_pipe.run()

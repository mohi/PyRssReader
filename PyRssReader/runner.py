from cmdline_parser import CmdlineParserBuilder

class Runner:
    """
    """
    def __init__(self):
        pass

    def runCmdline(self):
        cmdline_parser = CmdlineParserBuilder().build()
        args = cmdline_parser.inferArgs()
        from pipeline import Pipeline
        job_pipe = Pipeline()
        job_pipe.setInputReader(args.input_info)
        job_pipe.setConverters(args.convert_info)
        job_pipe.setOutputWriter(args.output_info)
        print(job_pipe.__dict__)
        job_pipe.run()


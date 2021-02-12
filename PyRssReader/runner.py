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
        job_pipe.setInputReader(args.input_src, \
                             args.input_type)
        job_pipe.setConverters(args.convert)
        job_pipe.setOutputWriter(args.output_src, \
                                   args.output_type)
        print(job_pipe.__dict__)
        job_pipe.run()

    def runManual(self, \
                   input_src = 'http://tech.uzabase.com/', \
                   input_type = 'url', \
                   converters = ['cut', 'replace(/abc/def/)'], \
                   output_src = 'result.txt', \
                   output_type = 'file', \
                   ):
        job_pipe = Pipeline()
        job_pipe.setInputReader(input_src, input_type)
        job_pipe.setConverters(converters)
        job_pipe.setOutputWriter(output_src, output_type)
        print(job_pipe.__dict__)
        job_pipe.run()


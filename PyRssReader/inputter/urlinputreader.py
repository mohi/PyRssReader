from PyRssReader.inputter.inputreaderinterface import InputReaderInterface


class UrlInputReader(InputReaderInterface):
    """
    Implements text reader from Rss feed Url
    """
    def __init__(self, input_src):
        self.__src_url = input_src
        self.__process_url()

    def __process_url(self):
        self.__src_url = self.__src_url + 'feed'

    def read(self):
        import requests
        response = requests.get(self.__src_url,
                                headers={'accept': 'application/xml'})
        data = response.text
        return data

""" Client module for the API wrapper.
    The config parser code will eventually be moved out
    of this module. It is only here so that this development
    version of the API wrapper can be easily tested without having to
    also create a test application
"""
import ConfigParser


class Client(object):
    def __init__(self, api_key):
        self.api_key = api_key


if __name__ == '__main__':
    config = ConfigParser.ConfigParser()
    config.readfp(open('traffic.conf'))
    api_key = config.get('API', 'KEY')



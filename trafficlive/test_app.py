import ConfigParser

from trafficlive import client


if __name__ == '__main__':
    config = ConfigParser.ConfigParser()
    config.readfp(open('traffic.conf'))
    api_key = config.get('API', 'KEY')
    client = client.Client(api_key=api_key)
    client.get_employee_list()


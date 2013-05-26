""" Client module for the API wrapper.
"""
from trafficlive import api, connection


class Client(object):
    def __init__(self, api_key):
        self.api_key = api_key
        self.connection = connection.Connection('https://production-sohnar.apigee.com/TrafficLiteServer/openapi', api_key)

    def get_employee_list(self):
        employee_data = api.StaffEmployee(self.connection).get_staff_list()
        print employee_data


class Employee(object):
    def __init__(self):
        pass


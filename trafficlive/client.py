""" Client module for the API wrapper.
"""
from trafficlive import api, connection


class Client(object):
    def __init__(self, api_key, username):
        self.api_key = api_key
        self.connection = connection.Connection(
                'https://api.sohnar.com/TrafficLiteServer/openapi', api_key, username)
        self.username = username

    def get_employee_list(self):
        employee_data = api.StaffEmployee(self.connection).get_staff_list()
        page_number = employee_data['currentPage']
        employee_list = []
        for employee_item in employee_data['resultList']:
            employee_list.append(Employee(employee_item))
        return employee_list


class Employee(object):
    def __init__(self, data):
        """ Data should be a json entry containing employee information
        """
        import ipdb
        ipdb.set_trace()
        self.username = data['userName']
        self.job_title = data['employeeDetails']['jobTitle']
        self.first_name = data['employeeDetails']['personalDetails']['firstName']
        self.last_name = data['employeeDetails']['personalDetails']['lastName']


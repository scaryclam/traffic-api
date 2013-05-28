""" Client module for the API wrapper.
"""
from trafficlive import api, connection


class Client(object):
    def __init__(self, api_key, username):
        self.api_key = api_key
        self.connection = connection.Connection(
                'https://api.sohnar.com/TrafficLiteServer/openapi', api_key, username)
        self.username = username

    def get_employee_list(self, window_size=None):
        employee_data = api.StaffEmployee(self.connection).get_staff_list(window_size=window_size)
        page_number = employee_data['currentPage']
        employee_list = []
        for employee_item in employee_data['resultList']:
            employee_list.append(Employee(employee_item))
        return employee_list

    def get_employee_id(self, pk):
        employee_data = api.StaffEmployee(self.connection).get_by_id(pk)
        return Employee(employee_data)


class Employee(object):
    def __init__(self, data):
        """ Data should be a json entry containing employee information
        """
        self.username = data['userName']
        self.active = data['active']
        self.date_modified = data['dateModified']
        self.version = data['version']
        self.staff_id = data['id']
        self.staff_class = data.get('@class', None)
        self.owner_company_id = data['ownerCompanyId']

        self.hours_worked_per_day_minutes = data['employeeDetails']['hoursWorkedPerDayMinutes']
        self.job_title = data['employeeDetails']['jobTitle']
        self.first_name = data['employeeDetails']['personalDetails']['firstName']
        self.last_name = data['employeeDetails']['personalDetails']['lastName']

    def get_time_calendar_blocks(self, conn):
        """ NOTE: conn may be removed when a refactor is done
        """
        cal_blocks = []
        data = api.TimeAllocationsCalendarBlocks(conn).get_by_employee(self.staff_id)
        for block in data['resultList']:
            cal_blocks.append(TimeAllocationCalendarBlock(block))

        return cal_blocks


class TimeAllocationCalendarBlock(object):
    def __init__(self, data):
        self.allocation_intervals = data['allocationIntervals']
        self.cal_block_list_item_id = data['calendarBlockListItemId']
        self.created_by_user_id = data['createdByUserId']['id']
        self.created_in_external_cal = data['createdInExternalCalendar']
        self.date_modified = data['dateModified']
        self.description = data['description']
        self.external_cal_tag = data['externalCalendarTag']
        self.external_cal_uuid = data['externalCalendarUUID']
        self.external_recurring_event = data['externalRecurringEvent']
        self.cal_block_id = data['id']
        self.open_to_edit = data['openToEdit']
        self.traffic_employee_id = data['trafficEmployeeId']['id']
        self.uuid = data['uuid']
        self.version = data['version']


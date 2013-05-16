from datetime import datetime

from trafficlive.connection import Connection


def populate_params(window_size=None, , current_page=None, filter_by=None, order=None):
    params = {}
        if window_size:
            params['windowSize'] = window_size
        if current_page:
            params['currentPage'] = current_page
        if filter_by:
            params['filter'] = filter_by
        if order:
            params['order'] = order

    return params


class BaseApi(object):
    def __init__(self, connection):
        self.conn = connection

    def get_list(self, window_size=None, current_page=None, filter_by=None, order=None, data_format='json'):
        params = populate_params(window_size, current_page, filter_by, order)
        item_list = self.conn.get(self.url, params,
                                  headers={'Accept': 'application/json'})
        return item_list

    def get_by_id(self, pk, data_format='json'):
        url = "%s/%s" % (self.url, str(pk))
        item = self.conn.get(url, headers={'Accept': 'application/json'})
        return item

    def post(self, data):
        response = self.conn.post(self.url, body=simplejson.dumps(data),
                                  headers={'Accept': 'application/json', 'Content-type': 'appication/json'})
        return response

    def put(self, data):
        response = self.conn.put(self.url, body=simplejson.dumps(data),
                                 headers={'Accept': 'application/json', 'Content-type': 'appication/json'})
        return response


class StaffEmployee(BaseApi):
    url = '/staff/employee'

    def get_staff_list(self, window_size=None, current_page=None, filter_by=None, order=None, data_format='json'):
        return super(StaffEmployee, self).get_list(window_size, current_page, filter_by, order) 


class StaffDepartment(BaseApi):
    url = '/staff/department'

    def get_department_list(self, window_size=None, current_page=None, filter_by=None, order=None, data_format='json'):
        return super(StaffDepartment, self).get_list(window_size, current_page, filter_by, order)


class StaffLocation(BaseApi):
    url = '/staff/location'

    def get_location_list(self, window_size=None, current_page=None, filter_by=None, order=None, data_format='json'):
        return super(StaffLocation, self).get_list(window_size, current_page, filter_by, order)


class Job(BaseApi):
    url = '/job'

    def get_itemtype(self, itemtype, pk):
        url = "%s/%s/%s" % (self.url, itemtype, pk)
        response = self.conn.get(url, headers={'Accept': 'application/json'})
        return response


class JobDetail(BaseApi):
    url = '/jobdetail'


class Project(BaseApi):
    url = '/project'


class Quote(BaseApi):
    url = '/quote'


class ChargeBand(BaseApi):
    url = '/chargeband'


class ChargeBandCustomRateSet(BaseApi):
    url = '/chargeband/customrateset'


class TimeEntries(BaseApi):
    url = '/timeentries'

    def get_list(self, start_date, end_date, window_size=None, current_page=None, filter_by=None, order=None, data_format='json'):
        params = populate_params(window_size, current_page, filter_by, order)
        params['startDate'] = start_date
        params['endDate'] = end_date

        item_list = self.conn.get(self.url, params,
                                  headers={'Accept': 'application/json'})
        return item_list

    def post_batch(self, data, force_update=False):
        url = "%s/%s" % (self.url, 'batch')
        response = self.conn.post(url, body=simplejson.dumps(data),
                                  headers={'Accept': 'application/json', 'Content-type': 'appication/json'})


class TimeAllocations(BaseApi):
    url = '/timeallocations/jobtasks'


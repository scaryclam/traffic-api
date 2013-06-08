from datetime import datetime

from trafficlive.connection import Connection


def populate_params(window_size=None, current_page=None, filter_by=None, order=None):
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
                                  headers={'Accept': 'application/json', 'Content-type': 'application/json'})
        return response

    def put(self, data):
        response = self.conn.put(self.url, body=simplejson.dumps(data),
                                 headers={'Accept': 'application/json', 'Content-type': 'application/json'})
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

    def get_list(self, start_date=None, end_date=None, window_size=None, current_page=None, filter_by=None, order=None, data_format='json'):
        params = populate_params(window_size, current_page, filter_by, order)
        params['startDate'] = start_date.strftime('%Y-%m-%d')
        params['endDate'] = end_date.strftime('%Y-%m-%d')

        item_list = self.conn.get(self.url, params,
                                  headers={'Accept': 'application/json'})
        return item_list['resultList'], item_list['currentPage']

    def post_batch(self, data, force_update=False):
        url = "%s/%s" % (self.url, 'batch')
        response = self.conn.post(url, body=simplejson.dumps(data),
                                  headers={'Accept': 'application/json', 'Content-type': 'appication/json'})


class TimeAllocations(BaseApi):
    url = '/timeallocations/jobtasks'

    def delete(self, pk):
        url = "%s/%s" % (self.url, pk)
        response = self.conn.delete(url)
        return response


class TimeAllocationsCalendarBlocks(BaseApi):
    url = '/timeallocations/calendarblocks'

    def delete(self,  pk):
        url = "%s/%s" % (self.url, pk)
        response = self.conn.delete(url)
        return response

    def get_by_employee(self, employee_pk):
        url = "/staff/employee/%s/calendarblockallocations" % employee_pk
        response = self.conn.get(url, headers={'Accept': 'application/json'})
        return response


class CrmClient(BaseApi):
    url = '/crm/client'

    def get_location_by_id(self, pk):
        url = "%s/%s/locations" % (self.url, pk)
        response = self.conn.get(url, headers={'Accept': 'application/json'})
        return response


class CrmSupplier(BaseApi):
    url = '/crm/supplier'

    def get_location_by_id(self, pk):
        url = "%s/%s/locations" % (self.url, pk)
        response = self.conn.get(url, headers={'Accept': 'application/json'})
        return response


class CrmOther(BaseApi):
    url = '/crm/other'

    def get_location_by_id(self, pk):
        url = "%s/%s/locations" % (self.url, pk)
        response = self.conn.get(url, headers={'Accept': 'application/json'})
        return response


class CrmAddress(BaseApi):
    url = '/crm/address'

    def get_list(self, parent_type='CLIENT', window_size=None, current_page=None, filter_by=None, order=None, data_format='json'):
        params = populate_params(window_size, current_page, filter_by, order)
        params['type'] = parent_type

        item_list = self.conn.get(self.url, params,
                                  headers={'Accept': 'application/json'})
        return item_list 


class CrmEmployee(BaseApi):
    url = '/crm/employee'

    def get_list(self, parent_type='CLIENT', window_size=None, current_page=None, filter_by=None, order=None, data_format='json'):
        params = populate_params(window_size, current_page, filter_by, order)
        params['type'] = parent_type
   
        item_list = self.conn.get(self.url, params,
                                  headers={'Accept': 'application/json'})
        return item_list


class ListItem(object):
    url = '/listitem'

    def __init__(self, connection):
        self.conn = connection

    def get_list(self, item_type, window_size=5, current_page=1):
        url = "%s/%s" % (self.url, item_type)
        params = {}
        params['windowSize'] = window_size
        params['currentPage'] = current_page

        item_list = self.conn.get(url, headers={'Accept': 'application/json'})
        return item_list

    def get_list_by_id(self, item_type, pk):
        url = "%s/%s/%s" % (self.url, item_type, pk)
        
        item_list = self.conn.get(url, headers={'Accept': 'application/json'})
        return item_list

    def post(self, item_type, data):
        url = "%s/%s" % (self.url, item_type)
        response = self.conn.post(url, body=data,
                                  headers={'Accept': 'application/json', 'Content-type': 'application/json'})
        return response

    def put(self, item_type, data):
        url = "%s/%s" % (self.url, item_type)
        response = self.conn.post(url, body=data,
                                  headers={'Accept': 'application/json', 'Content-type': 'application/json'})
        return response

    def delete(self, item_type, pk):
        url = "%s/%s/%s" % (self.url, item_type, pk)
        response = self.conn.delete(url)
        return response


class Tag(BaseApi):
    url = '/tag'

    def delete(self, pk):
        url = '%s/%s' % (self.url, str(pk))
        response = self.conn.delete(url)
        return response


class TaxType(BaseApi):
    url = '/taxtype'

    def delete(self, pk):
        url = '%s/%s' % (self.url, pk)
        response = self.conn.delete(url)
        return response


class ApplicationCountry(object):
    url = '/application/country'

    def __init__(self, connection):
        self.conn = connection

    def get_list(self, window_size=None, current_page=None, filter_by=None, order=None, data_format='json'):
        params = populate_params(window_size, current_page, filter_by, order)
        item_list = self.conn.get(self.url, params,
                                  headers={'Accept': 'application/json'})
        return item_list


class InvoiceItems(BaseApi):
    url = '/invoice/items'


class Order(BaseApi):
    url = '/order'

    def delete(self, pk):
        url = "%s/%s" % (self.url, str(pk))
        response = self.conn.delete(url)
        return response


from trafficlive.connection import Connection


class StaffEmployee(object):
    url = '/staff/employee/'

    def __init__(self, connection):
        self.conn = connection

    def get_list(self, window_size=None, current_page=None, filter_by=None, order=None, data_format='json'):
        params = {}
        if window_size:
            params['windowSize'] = window_size
        if current_page:
            params['currentPage'] = current_page
        if filter_by:
            params['filter'] = filter_by
        if order:
            params['order'] = order

        staff_list = self.conn.get(self.url, params, headers={'Accept': 'application/json'})
        return staff_list

    def get_by_id(self, pk, data_format='json'):
        url = "%s%s" % (self.url, str(pk))
        staff_member = self.conn.get(url, headers={'Accept': 'application/json'})
        return staff_member

    def post(self):
        pass

    def put(self):
        pass


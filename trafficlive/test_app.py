import os
import ConfigParser
from datetime import datetime, timedelta

from trafficlive import client as trafficlive_client


def get_client():
    config = ConfigParser.ConfigParser()
    config.readfp(open(os.path.join(os.path.dirname(__file__), 'traffic.conf')))
    api_key = config.get('API', 'KEY')
    username = config.get('API', 'USERNAME')
    client = trafficlive_client.Client(api_key, username)
    return client


def get_one_weeks_time(employee_id, start_date, client):
    filter_str = 'trafficEmployeeId|EQ|%s' % str(employee_id)
    end_date = start_date + timedelta(days=7)
    blocks = client.get_time_entry_list(filter_by=filter_str,
                                        start_date=start_date,
                                        end_date=end_date)
    return blocks


if __name__ == '__main__':
    client = get_client()
    employee_id = 1234
    start_date = datetime(day=03, month=06, year=2013) - timedelta(days=7)
    time_entries = get_one_weeks_time(employee_id, start_date, client)
    for entry in time_entries:
        job = client.get_job_id(entry.job_id)
        job.get_job_detail(client.connection)
        print "-" * 30
        print "Job Number", job.job_number
        print "Start Time:", entry.start_time
        print "End Time:", entry.end_time
        print "Task Description", entry.task_description
        print "Job Name", job.job_detail.name
        print "-" * 30

    import ipdb
    ipdb.set_trace()


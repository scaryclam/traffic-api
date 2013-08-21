from unittest import TestCase

from trafficlive.client import TimeEntry


class TestTimeEntry(TestCase):
    def test_create_new_json(self):
        data = {
            'id': 1,
            'version': 1,
            'dateModified': None,
            'jobTaskId': {'id': 1},
            'billable': False,
            'exported': False,
            'lockedByApproval': False,
            'comment': "Comment!",
            'endTime': "2013-07-22T12:30:00.000+0000",
            'minutes': 120,
            'trafficEmployeeId': {'id': 1},
            'taskDescription': "This is a task",
            'taskComplete': False,
            'taskRate': 123,
            'valueOfTimeEntry': 123 * 120,
            'jobId': {'id': 1},
            'chargeBandId': 1,
            'timeEntryCost': 123,
            'timeEntryPersonalRate': 123,
            'jobStageDescription': "Dev",
            'lockedByApprovalEmployeeId': None,
            'lockedByApprovalDate': None,
            'exportError': None,
            'workPoints': None,
            'startTime': "2013-07-22T11:00:00.000+0000",
        }
        entry = TimeEntry(data)
        print entry.create_payload()
        self.assertTrue(False)


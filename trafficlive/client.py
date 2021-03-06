""" Client module for the API wrapper.
"""
from trafficlive import api, connection


class Client(object):
    def __init__(self, api_key, username, base_url=None):
        self.api_key = api_key
        if not base_url:
            base_url = 'https://api.sohnar.com/TrafficLiteServer/openapi'
        self.connection = connection.Connection(base_url, api_key, username)
        self.username = username

    def _get_list(self, api_method, obj_class, **kwargs):
        data = api_method(**kwargs)
        data_list = []
        current_page = data['currentPage']
        for item in data['resultList']:
            data_list.append(obj_class(item))
        return data_list, current_page

    def get_employee_list(self, window_size=None, current_page=None, filter_by=None, order=None):
        employee_list, page = self._get_list(api.StaffEmployee(self.connection).get_staff_list,
                                             Employee,
                                             window_size=window_size,
                                             current_page=current_page,
                                             filter_by=filter_by,
                                             order=order)
        return employee_list, page

    def get_employee_id(self, pk):
        employee_data = api.StaffEmployee(self.connection).get_by_id(pk)
        return Employee(employee_data)

    def get_project_list(self, window_size=None, current_page=None, filter_by=None, order=None):
        project_list, page = self._get_list(api.Project(self.connection).get_list,
                                            Project,
                                            window_size=window_size,
                                            current_page=current_page,
                                            filter_by=filter_by,
                                            order=order)
        return project_list, page

    def get_project_id(self, pk):
        project_data = api.Project(self.connection).get_by_id(pk)
        return Project(project_data)

    def get_job_list(self, window_size=None, current_page=None, filter_by=None, order=None):
        job_list, page = self._get_list(api.Job(self.connection).get_list,
                                        Job,
                                        window_size=window_size,
                                        current_page=current_page,
                                        filter_by=filter_by,
                                        order=order)
        return job_list, page

    def get_job_id(self, pk):
        job_data = api.Job(self.connection).get_by_id(pk)
        return Job(job_data)

    def get_time_entry_list(self, window_size=None, current_page=None, filter_by=None, order=None, start_date=None, end_date=None):
        time_entry_list, page = self._get_list(api.TimeEntries(self.connection).get_list,
                                               TimeEntry,
                                               window_size=window_size,
                                               current_page=current_page,
                                               filter_by=filter_by,
                                               order=order,
                                               start_date=start_date,
                                               end_date=end_date)
        return time_entry_list

    def get_time_allocation_list(self, window_size=None, current_page=None, filter_by=None, order=None):
        time_allocation_list, page = self._get_list(api.TimeAllocations(self.connection).get_list,
                                                    TimeAllocation,
                                                    window_size=window_size,
                                                    current_page=current_page,
                                                    filter_by=filter_by,
                                                    order=order)
        return time_allocation_list, page

    def send_new_time_entry(self, time_entry):
        result = api.TimeEntries(self.connection).put(time_entry.create_json_payload(create_new=True))
        return result.content

    def update_time_entry(self, time_entry):
        result = api.TimeEntries(self.connection).post(time_entry.create_json_payload())

    def get_time_entry(self, time_entry_pk):
        time_entry = api.TimeEntries(self.connection).get_by_id(time_entry_pk)
        return TimeEntry(time_entry)


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

    def get_time_calendar_blocks(self, conn, window_size=None, current_page=None, order=None):
        """ NOTE: conn may be removed when a refactor is done
        """
        cal_blocks = []
        data = api.TimeAllocationsCalendarBlocks(conn).get_by_employee(self.staff_id,
                                                                       window_size=window_size,
                                                                       current_page=current_page,
                                                                       order=order)
        for block in data['resultList']:
            cal_blocks.append(TimeAllocationCalendarBlock(block))

        return cal_blocks

    def get_time_entries(self, conn, start_date, end_date, window_size=None, current_page=None):
        filter_str = 'trafficEmployeeId|EQ|%s' % self.staff_id
        time_entries = []
        time_entry_list = api.TimeEntries(conn).get_list(window_size=window_size,
                                                         current_page=current_page,
                                                         filter_by=filter_str,
                                                         start_date=start_date,
                                                         end_date=end_date)
        for entry in time_entry_list['resultList']:
            time_entries.append(TimeEntry(entry))

        return time_entries

    def get_time_allocations(self, conn, window_size=None, current_page=None):
        filter_str = 'trafficEmployeeId|EQ|%s' % self.staff_id
        time_allocation_list = []
        data = api.TimeAllocations(conn).get_list(window_size=window_size,
                                                  current_page=current_page,
                                                  filter_by=filter_str)
        for item in data['resultList']:
            time_allocation_list.append(TimeAllocation(item))

        return time_allocation_list, data['currentPage']

    def get_job_task_allocations(self, conn, window_size=None, current_page=None):
        data = api.JobTaskAllocation(conn).get_by_employee(
            self.staff_id, window_size=window_size, current_page=current_page)
        #for item in data['resultList']:
        return data['resultList']


class JobTaskAllocationInterval(object):
    def __init__(self, data):
        self.uuid = data['uuid']
        self.allocation_interval_status = data['allocationIntervalStatus']
        self.date_modified = data['dateModified']
        self.version = 1
        self.duration_in_seconds = data['durationInSeconds']
        self.start_time = data['startTime']
        self.end_time = data['endTime']
        self.id = data['id']


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
        self.earliest_interval_start = data['earliestIntervalStart']
        self.latest_interval_end = data['latestIntervalEnd']


class TimeAllocation(object):
    def __init__(self, data):
        self.allocation_intervals = []
        for allocation in data['allocationIntervals']:
            self.allocation_intervals.append(JobTaskAllocationInterval(allocation))
        self.client_name = data['clientName']
        self.date_modified = data['dateModified']
        self.dependancy_task_deadline = data['dependancyTaskDeadline']
        self.duration_in_minutes = data['durationInMinutes']
        self.external_calendar_tag = data['externalCalendarTag']
        self.external_calendar_uuid = data['externalCalendarUUID']
        self.happy_rating = data['happyRating']
        self.time_allocation_id = data['id']
        self.is_task_complete = data['isTaskComplete']
        self.is_task_milestone = data['isTaskMilesone']
        self.job_id = data['jobId']
        self.job_name = data['jobName']
        self.job_number_search_wrapper = data['jobNumberSearchWrapper']
        self.job_stage_description = data['jobStageDescription']
        self.job_stage_uuid = data['jobStageUUID']
        self.job_task_id = data['jobTaskId']
        self.task_deadline = data['taskDeadline']
        self.task_description = data['taskDescription']
        self.total_time_logged_in_minutes = data['totalTimeLoggedMinutes']
        self.traffic_employee_id = data['trafficEmployeeId']
        self.uuid = data['uuid']
        self.version = data['version']


class Project(object):
    def __init__(self, data):
        self.client_crm_entry_id = data['clientCRMEntryId']
        self.date_modified = data['dateModified']
        self.project_id = data['id']
        self.project_name = data['name']
        self.version = data['version']


class Job(object):
    def __init__(self, data):
        self.applied_custom_date_set_id = data['appliedCustomRateSetId']
        self.billed_job = data['billableJob']
        self.billed_net = data['billedNet']
        self.billed_tax_one_amount = data['billedTaxOneAmount']
        self.billed_tax_two_amount = data['billedTaxTwoAmount']
        self.client_purchased_order_value = data['clientPurchaseOrderValue']
        self.client_reference = data['clientReference']
        self.date_created = data['dateCreated']
        self.date_modified = data['dateModified']
        self.external_code = data['externalCode']
        self.external_deadline = data['externalDeadline']
        self.free_tags = data['freeTags']
        self.job_id = data['id']
        self.internal_deadline = data['internalDeadline']
        self.invoices = data['invoices']
        self.job_billing_state_type = data['jobBillingStateType']
        self.job_completed_date = data['jobCompletedDate']
        self.job_detail_id = data['jobDetailId']
        self.job_expenses = data['jobExpenses']
        self.job_number = data['jobNumber']
        self.job_stages = data['jobStages']
        self.job_state_type = data['jobStateType']
        self.job_tasks = data['jobTasks']
        self.job_third_party_costs = data['jobThirdPartyCosts']
        self.job_category_list_item_id = data['jobUserCategoryListItemId']
        self.last_updated_user_id = data['lastUpdatedUserId']
        self.multi_currency_edit_mode = data['multiCurrencyEditMode']
        self.multi_currency_sync_mode = data['multiCurrencySyncMode']
        self.multi_currency_enabled = data['multicurrencyEnabled']
        self.multi_currency_rate = data['multicurrencyRate']
        self.other_currency = data['otherCurrency']
        self.secondary_external_code = data['secondaryExternalCode']
        self.tcid = data.get('tcId', None)
        self.version = data['version']
        self.job_detail = None

    def get_job_detail(self, conn):
        data = api.JobDetail(conn).get_by_id(self.job_detail_id)
        self.job_detail = JobDetail(data)
        return self.job_detail


class JobDetail(object):
    def __init__(self, data):
        self.account_manager_id = data['accountManagerId']
        self.date_modified = data['dateModified']
        self.description = data['description']
        self.job_detail_id = data['id']
        self.job_contact_id = data['jobContactId']
        self.job_cost_type = data['jobCostType']
        self.job_description = data['jobDescription']
        self.job_type_list_item_id = data['jobTypeListItemId']
        self.last_updated_user_id = data['lastUpdatedUserId']
        self.name = data['name']
        self.notes = data['notes']
        self.owner_project_id = data['ownerProjectId']
        self.version = data['version']


class TimeEntry(object):
    def __init__(self, data):
        self.time_entry_id = data['id']
        self.version = data['version']
        self.date_modified = data['dateModified']
        self.job_task_id = data['jobTaskId']['id']
        self.billable = data['billable']
        self.exported = data['exported']
        self.locked_by_approval = data['lockedByApproval']
        self.comment = data['comment']
        self.end_time = data['endTime']
        self.minutes = data['minutes']
        self.traffic_employee_id = data['trafficEmployeeId']['id']
        self.task_description = data['taskDescription']
        self.task_complete = data['taskComplete']
        self.task_rate = data['taskRate']
        self.value_of_time_entry = data['valueOfTimeEntry']
        self.job_id = data['jobId']['id']
        if data.get('allocationGroupId', False):
            self.allocation_group_id = data['allocationGroupId']['id']
        else:
            self.allocation_group_id = None
        self.charge_band_id = data['chargeBandId']
        self.time_entry_cost = data['timeEntryCost']
        self.time_entry_personal_rate = data['timeEntryPersonalRate']
        self.job_stage_description = data['jobStageDescription']
        self.locked_by_approval_employee_id = data['lockedByApprovalEmployeeId']
        self.locked_by_approval_date = data['lockedByApprovalDate']
        self.export_error = data['exportError']
        self.work_points = data['workPoints']
        self.start_time = data['startTime']

        if not self.time_entry_personal_rate['currencyType']:
            self.time_entry_personal_rate['currencyType'] = u'GBP'
        if not self.time_entry_personal_rate['amountString']:
            self.time_entry_personal_rate['amountString'] = u'0.0'

    def create_json_payload(self, create_new=False):
        """ Creates a custom json payload
        """
        payload = {
            "jobId": {"id": self.job_id},
            #"allocationGroupId": {"id": self.allocation_group_id},
            "jobStageDescription": self.job_stage_description,
            "timeEntryCost": self.time_entry_cost,
            "timeEntryPersonalRate": self.time_entry_personal_rate,
            "valueOfTimeEntry": self.value_of_time_entry,
            "exported": self.exported,
            "lockedByApproval": self.locked_by_approval,
            "endTime": self.end_time,
            "workPoints": self.work_points,
            "billable": self.billable,
            "version": self.version,
            "startTime": self.start_time,
            "id": self.time_entry_id,
            "jobTaskId": {"id": self.job_task_id},
            "trafficEmployeeId": {"id": self.traffic_employee_id},
            "taskDescription": self.task_description,
            "chargeBandId": self.charge_band_id,
            "minutes": self.minutes,
            "lockedByApprovalEmployeeId": self.locked_by_approval_employee_id,
            "exportError": self.export_error,
            "taskRate": self.task_rate,
            "taskComplete": self.task_complete,
            "lockedByApprovalDate": self.locked_by_approval_date,
            "comment": self.comment
        }
        if not create_new:
            payload['dateModified'] = self.date_modified

        return payload

    def create_payload(self, payload_type='json'):
        if payload_type == 'json':
            return self.create_json_payload()


class ChargeBand(object):
    pass

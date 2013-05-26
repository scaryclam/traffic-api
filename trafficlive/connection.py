import simplejson
import requests


class Connection(object):
    def __init__(self, base_url, api_key, username):
        self.base_url = base_url
        self.api_key = api_key
        self.username = username

    def get(self, url, params, headers=None):
        full_url = self._build_url(url)
        if not headers:
            headers = {}
        response = requests.get(full_url, headers=headers, auth=(self.username, self.api_key))
        return simplejson.loads(response.content)

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass

    def _build_url(self, url):
        return "%s%s" % (self.base_url, url)


class DummyConnection(Connection):
    """ Connection class that returns mock data.
        This is for testing stuff out until I get
        the api key.
    """

    def get(self, url, params, headers):
        return simplejson.loads("""{
   "maxResults":17,
   "resultList":[
      {
         "@class":"com.sohnar.trafficlite.transfer.trafficcompany.TrafficEmployeeTO",
         "id":1,
         "version":0,
         "dateModified":null,
         "locationId":1,
         "departmentId":1,
         "ownerCompanyId":1,
         "active":false,
         "userId":null,
         "userName":null,
         "externalCode":"externalCode:1-4bb5-8",
         "employeeDetails":{
            "id":1,
            "version":0,
            "dateModified":null,
            "jobTitle":"Chairman",
            "costPerHour":{
               "amountString":80.00,
               "currencyType":"GBP"
            },
            "hoursWorkedPerDayMinutes":450,
            "hoursWorkedPerDayBillableMinutes":null,
            "personalDetails":{
               "id":1,
               "version":0,
               "dateModified":null,
               "titleType":null,
               "firstName":"Jeremy",
               "middleName":null,
               "lastName":"Rudge",
               "emailAddress":"jeremy@sohnar.com",
               "workPhone":null,
               "mobilePhone":null,
               "faxPhone":null,
               "homePhone":null
            },
            "emailSignature":null,
            "defaultGroupModeOn":true,
            "trafficEmployeeCalendar":null
         },
         "chargeBandAllocationsIds":[
            
         ],
         "personalRateChargeBandId":null,
         "employeeGroupIds":[
            
         ],
         "isResource":false
      },
      {
         "@class":"com.sohnar.trafficlite.transfer.trafficcompany.TrafficEmployeeTO",
         "id":2,
         "version":0,
         "dateModified":null,
         "locationId":1,
         "departmentId":1,
         "ownerCompanyId":1,
         "active":false,
         "userId":null,
         "userName":null,
         "externalCode":"externalCode:fdff76d0",
         "employeeDetails":{
            "id":2,
            "version":0,
            "dateModified":null,
            "jobTitle":"Senior Developer",
            "costPerHour":{
               "amountString":45.00,
               "currencyType":"GBP"
            },
            "hoursWorkedPerDayMinutes":450,
            "hoursWorkedPerDayBillableMinutes":null,
            "personalDetails":{
               "id":2,
               "version":0,
               "dateModified":null,
               "titleType":null,
               "firstName":"Simon",
               "middleName":null,
               "lastName":"Stewart",
               "emailAddress":"simon@sohnar.com",
               "workPhone":null,
               "mobilePhone":null,
               "faxPhone":null,
               "homePhone":null
            },
            "emailSignature":null,
            "defaultGroupModeOn":true,
            "trafficEmployeeCalendar":null
         },
         "chargeBandAllocationsIds":[
            
         ],
         "personalRateChargeBandId":null,
         "employeeGroupIds":[
            
         ],
         "isResource":false
      },
      {
         "@class":"com.sohnar.trafficlite.transfer.trafficcompany.TrafficEmployeeTO",
         "id":3,
         "version":0,
         "dateModified":null,
         "locationId":1,
         "departmentId":1,
         "ownerCompanyId":1,
         "active":false,
         "userId":null,
         "userName":null,
         "externalCode":"externalCode:1a8446b3",
         "employeeDetails":{
            "id":3,
            "version":0,
            "dateModified":null,
            "jobTitle":"User Experience Architect",
            "costPerHour":{
               "amountString":45.00,
               "currencyType":"GBP"
            },
            "hoursWorkedPerDayMinutes":450,
            "hoursWorkedPerDayBillableMinutes":null,
            "personalDetails":{
               "id":3,
               "version":0,
               "dateModified":null,
               "titleType":null,
               "firstName":"Matt",
               "middleName":null,
               "lastName":"Auld",
               "emailAddress":"matt@sohnar.com",
               "workPhone":null,
               "mobilePhone":null,
               "faxPhone":null,
               "homePhone":null
            },
            "emailSignature":null,
            "defaultGroupModeOn":true,
            "trafficEmployeeCalendar":null
         },
         "chargeBandAllocationsIds":[
            
         ],
         "personalRateChargeBandId":null,
         "employeeGroupIds":[
            
         ],
         "isResource":false
      },
      {
         "@class":"com.sohnar.trafficlite.transfer.trafficcompany.TrafficEmployeeTO",
         "id":4,
         "version":0,
         "dateModified":null,
         "locationId":1,
         "departmentId":1,
         "ownerCompanyId":1,
         "active":false,
         "userId":null,
         "userName":null,
         "externalCode":"externalCode:131724a0",
         "employeeDetails":{
            "id":4,
            "version":0,
            "dateModified":null,
            "jobTitle":"Flex Developer",
            "costPerHour":{
               "amountString":40.00,
               "currencyType":"GBP"
            },
            "hoursWorkedPerDayMinutes":450,
            "hoursWorkedPerDayBillableMinutes":null,
            "personalDetails":{
               "id":4,
               "version":0,
               "dateModified":null,
               "titleType":null,
               "firstName":"Martin",
               "middleName":null,
               "lastName":"McBrearty",
               "emailAddress":"martin@mcbrearty.me.uk",
               "workPhone":null,
               "mobilePhone":null,
               "faxPhone":null,
               "homePhone":null
            },
            "emailSignature":null,
            "defaultGroupModeOn":true,
            "trafficEmployeeCalendar":null
         },
         "chargeBandAllocationsIds":[
            
         ],
         "personalRateChargeBandId":null,
         "employeeGroupIds":[
            
         ],
         "isResource":false
      },
      {
         "@class":"com.sohnar.trafficlite.transfer.trafficcompany.TrafficEmployeeTO",
         "id":5,
         "version":0,
         "dateModified":null,
         "locationId":1,
         "departmentId":1,
         "ownerCompanyId":1,
         "active":false,
         "userId":null,
         "userName":null,
         "externalCode":"externalCode:40b78313",
         "employeeDetails":{
            "id":5,
            "version":0,
            "dateModified":null,
            "jobTitle":"Flex Developer",
            "costPerHour":{
               "amountString":40.00,
               "currencyType":"GBP"
            },
            "hoursWorkedPerDayMinutes":450,
            "hoursWorkedPerDayBillableMinutes":null,
            "personalDetails":{
               "id":5,
               "version":0,
               "dateModified":null,
               "titleType":null,
               "firstName":"Tom",
               "middleName":null,
               "lastName":"Fryer",
               "emailAddress":"tom@sohnar.com",
               "workPhone":null,
               "mobilePhone":null,
               "faxPhone":null,
               "homePhone":null
            },
            "emailSignature":null,
            "defaultGroupModeOn":true,
            "trafficEmployeeCalendar":null
         },
         "chargeBandAllocationsIds":[
            
         ],
         "personalRateChargeBandId":null,
         "employeeGroupIds":[
            
         ],
         "isResource":false
      }
   ],
   "windowSize":5,
   "currentPage":1
}
""")

    



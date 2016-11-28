# Written using Python 2.7.12
# Code2040's 2017 Fellows Application
# Step V: The dating game

import requests
import json
import datetime, time
from json import dumps
from secret import token		# token value is stored in a file saved locally called secret

header = {'Content-Type': 'application/json'}

# URL to recieve the dictionary for the datestamp
dating_api_url = 'http://challenge.code2040.org/api/dating'

# URL to validate new datestamp
validate_api_url = 'http://challenge.code2040.org/api/dating/validate'

body_1 = {'token': token}
response_1 = requests.post(dating_api_url, data = dumps(body_1), headers = header)

# assigns datestamp variable to the datestamp recieved from the API
date = response_1.json()['datestamp']

# assigns the interval variable to the inverval recieved from the API
interval = response_1.json()['interval']      

print 'datestamp: ', date, '\n'
print 'interval: ', interval, ' (seconds)', '\n'

# convert date datestamp to datetime object to make conversion easier
date = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ")
print 'date as datetime object: ', date, '\n'

# adding interval to date using timedelta()
date += datetime.timedelta(seconds = interval)
print 'date with interval added: ', date, '\n'

# convert date to ISO 8601 formated string and add 'Z'
datestamp = str(date.isoformat()) + 'Z'
print 'datestamp as ISO 8601 formated string: ', datestamp, '\n'

body_2 = {'token' : token, 'datestamp' : datestamp}
response_2 = requests.post(validate_api_url, data = dumps(body_2), headers = header)

print response_2.text		# Step 5 complete

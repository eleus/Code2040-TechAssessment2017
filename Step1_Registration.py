# Written using Python 2.7.12
# Code2040's 2017 Fellows Application
# Step I: Registration

import requests
from json import dumps
from secret import token		# token value is stored in a file saved locally called secret

header = {'Content-Type': 'application/json'}

# URL to register
register_api_url = 'http://challenge.code2040.org/api/register'

body = {'token': token, 'github' : 'https://github.com/eleus/Code2040-TechAssessment2017'}
response = requests.post(register_api_url, data = dumps(body), headers = header)

print response.text

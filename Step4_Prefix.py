# Written using Python 2.7.12
# Code2040's 2017 Fellows Application
# Step IV: Prefix

import requests
import json
from json import dumps
from secret import token		# token value is stored in a file saved locally called secret

header = {'Content-Type': 'application/json'}

# URL to recieve prefix
prefix_api_url = 'http://challenge.code2040.org/api/prefix'

# URL to validate new array/list
validate_api_url = 'http://challenge.code2040.org/api/prefix/validate'

body_1 = {'token': token}
response_1 = requests.post(prefix_api_url, data = dumps(body_1), headers = header)
print response_1.text

dictionary = json.loads(response_1.text)
array = dictionary['array']           # assigns the list from the 'array' key from the dictionary to the variable array
prefix = dictionary['prefix']         # assigns the value associated to 'prefix' from the dictionary to the variable prefix
newArray = []                         # in fact, this is a list, not an array as the name suggests

for string in array:
    string = string.encode('UTF8')      	# converts string from unicode to UTF8
    if not string.startswith(prefix):   	# i.e. string doesn't start with prefix
        newArray += [string]
        
print 'array: ', array, '\n'
print 'prefix: ', prefix, '\n'
print 'newArray: ', newArray, '\n'

body_2 = {'token' : token, 'array' : newArray}
response_2 = requests.post(validate_api_url, data = dumps(body_2), headers = header)

print response_2.text		# Step 4 complete

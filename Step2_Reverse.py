# Written using Python 2.7.12
# Code2040's 2017 Fellows Application
# Step II: Reverse a string

import requests
from json import dumps
from secret import token		# token value is stored in a file saved locally called secret

header = {'Content-Type': 'application/json'}

# URL to recieve string
reverse_api_url = 'http://challenge.code2040.org/api/reverse'

# URL to validate reversed string
validate_api_url = 'http://challenge.code2040.org/api/reverse/validate'

body_1 = {'token': token}
response_1 = requests.post(reverse_api_url, data = dumps(body_1), headers = header)

print 'The string to be reversed is: ', response_1.text

reversed_string = ''

for i in reversed(range(len(response_1.text))):			# iterates through the indices backwards
    reversed_string += response_1.text[i]

print 'The reversed string is: ', reversed_string

body_2 = {'token' : token, 'string' : reversed_string}
response_2 = requests.post(validate_api_url, data = dumps(body_2), headers = header)

print response_2.text		# Step 2 complete

# This can be done multiple ways, such as using the reversed() function, slicing, or recursion.

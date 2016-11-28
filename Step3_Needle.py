# Written using Python 2.7.12
# Code2040's 2017 Fellows Application
# Step III: Needle in a haystack

import requests
from json import dumps
from secret import token		# token value is stored in a file saved locally called secret

header = {'Content-Type': 'application/json'}

# URL to recieve dictionary
dict_api_url = 'http://challenge.code2040.org/api/haystack'

# URL to to validate the needle's index
validate_api_url = 'http://challenge.code2040.org/api/haystack/validate'

body_1 = {'token': token}
response_1 = requests.post(dict_api_url, data = dumps(body_1), headers = header)

haystack = response_1.json()['haystack']    # assigns the list from the 'haystack' key from the dictionary to the variable haystack
needle = response_1.json()['needle']        # assigns the value associated to 'needle' from the dictionary to needle
index = haystack.index(needle)              # assigns the 'index' variable to the index of the first instance of needle in the list haystack 

body_2 = {'token' : token, 'needle' : index}
response_2 = requests.post(validate_api_url, data = dumps(body_2), headers = header)

print response_2.text		# Step 3 complete

import requests 

endpoint = 'http://httpbin.org/status/200'
endpoint = 'http://httpbin.org/anything'

# HTTP response
get_response = requests.get(endpoint, json={'query':'hello world'})
#  print raw text response
# print(get_response.text)
print(get_response.json())          # python dict
print(get_response.status_code)

import requests 

#endpoint = 'http://httpbin.org/status/200'
# endpoint = 'http://httpbin.org/anything'
endpoint = 'http://localhost:8000/api/'

# HTTP response
get_response = requests.get(endpoint, params={'hi': 'bella'}, json={'query':'hello world'})
#  print raw text response
# print(get_response.text)
print(get_response.json())          # python dict
print(get_response.status_code)

import requests 

#endpoint = 'http://httpbin.org/status/200'
# endpoint = 'http://httpbin.org/anything'
endpoint = 'http://localhost:8000/api/'

# HTTP response
get_response = requests.post(endpoint,  json={'title': 'Abc123', 'content': 'red pen', 'price': '100'})
# print(get_response.headers)
# print('...')
# print(get_response.text)
#  print raw text response
# print(get_response.text)

print(get_response.json())          # python dict
# print(get_response.status_code)

import requests 

endpoint = 'http://localhost:8000/api/products/1/'

# HTTP response
get_response = requests.get(endpoint)


print(get_response.json())          # python dict
# print(get_response.status_code)

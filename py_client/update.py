import requests

endpoint = 'http://localhost:8000/api/products/1/update/'

data = {
    'title': 'link pen',
    'price': 100
}

# HTTP response
get_response = requests.put(endpoint, json=data)

print(get_response.json())          # python dict
# print(get_response.status_code)

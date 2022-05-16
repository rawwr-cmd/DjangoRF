import requests

endpoint = 'http://localhost:8000/api/products/'

data = {
    'title': 'link pen',
    'price': 10
}
# HTTP response
get_response = requests.post(endpoint, data)


print(get_response.json())

import requests 

endpoint = 'http://localhost:8000/api/products/'

data = {
    'title' : 'my black Pen',
    'price' : 10
}
# HTTP response
get_response = requests.post(endpoint, data)


print(get_response.json())          
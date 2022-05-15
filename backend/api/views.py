# converting string into actual pyhon dictionary
import json

from django.http import  JsonResponse


def api_home(request, *args, **kwargs):
    # print(dir(request))
    print(request.GET)
    print(request.POST)
    body = request.body #byte string of JSON data
    data = {}
    try: 
        data = json.loads(body)  #String of JSON data -> Python Dict
    except:
        pass
    print(data)    
    # data['headers'] = request.headers # request.META

    data['params'] = dict(request.GET) 
    data['header'] = dict(request.headers)
    data['content-type'] = request.content_type
    # print(body)         #output b'{"query": "hello world"}'
    return JsonResponse(data)
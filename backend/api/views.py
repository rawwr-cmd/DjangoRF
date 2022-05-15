# converting string into actual pyhon dictionary
import json
from django.http import  JsonResponse

from products.models import Product


def api_home(request, *args, **kwargs):
    # getting a random product from products.models
    model_data = Product.objects.all().order_by('?').first()
    data={}
    if model_data:
        data['id'] = model_data.id                         # id-by_default
        data['title'] = model_data.title
        data['content'] = model_data.content
        data['price'] = model_data.price
    return JsonResponse(data)
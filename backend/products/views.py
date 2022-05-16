from rest_framework import generics

from .models import Product 
from .serializers import ProductSerializer


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # assigning data on createAPIView
    def perform_create(self, serializer):
        # print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        if content is None:
            content = title
        
        serializer.save(content=content)

product_list_create_view = ProductListCreateAPIView.as_view() 

class ProductDetailsAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    #lookup_field = 'pk'

product_detail_view = ProductDetailsAPIView.as_view()    

class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    #lookup_field = 'pk'

product_list_view = ProductListAPIView.as_view()   

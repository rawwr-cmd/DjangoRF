from rest_framework import authentication, generics, mixins, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.response import Response
# from django.http import Http404
from django.shortcuts import get_object_or_404

from .models import Product
from .permissions import IsStaffEditorPermission
from .serializers import ProductSerializer


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [
        authentication.SessionAuthentication, authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

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

    # lookup_field = 'pk'


product_detail_view = ProductDetailsAPIView.as_view()

# update


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        print(serializer)
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
            ##


product_update_view = ProductUpdateAPIView.as_view()

# delete


class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        # instance
        super().perform_destroy(instance)


product_destroy_view = ProductDestroyAPIView.as_view()

# class ProductListAPIView(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

#     # lookup_field = 'pk'


# product_list_view = ProductListAPIView.as_view()

# class based view
class ProductMixinView(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,  # for detailsview
                       generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):  # HTTP -> get
        print(args, kwargs)
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):  # HTTP -> post
        return self.create(request, *args, **kwargs)

    # or
    def perform_create(self, serializer):
        # print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        if content is None:
            content = 'this is a new model'

        serializer.save(content=content)


product_mixin_view = ProductMixinView.as_view()

# Using function based views for create Retrieve or List


@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method  # PUT -> update #Destroy -> delete

    if method == 'GET':
        if pk is not None:
            # detail view
            # in case object exists otherwise 404
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)

    # list view
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)

    if method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # print(serializer.validated_data)
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content')
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({"invalid": "not good data"}, status=400)

from rest_framework.generics import ListCreateAPIView
from .models import Product
from .serializer import ProductSerializer



class Product_view(ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
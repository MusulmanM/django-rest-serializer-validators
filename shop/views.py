from rest_framework.generics import ListCreateAPIView
from .serializer import Catserializer, Proserializer
from .models import Category, Product

# Create your views here.




class Catapiview(ListCreateAPIView):
    serializer_class = Catserializer
    queryset = Category.objects.all()




class Proapiview(ListCreateAPIView):
    serializer_class = Proserializer
    queryset = Product.objects.all()

    
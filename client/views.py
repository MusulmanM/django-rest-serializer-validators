from rest_framework.generics import ListCreateAPIView
from .serializer import MijozSerializer
from .models import Mijoz
# Create your views here.



class Mijozapiview(ListCreateAPIView):
    serializer_class = MijozSerializer
    queryset = Mijoz.objects.all()
    
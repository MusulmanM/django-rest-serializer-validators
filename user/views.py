from rest_framework.generics import ListCreateAPIView
from .serializer import Ucartserializer, UfavouriteSerializer, Postserializer
from .models import Usercart, UserFavourite, Post
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class Ucartapiview(ListCreateAPIView):
    serializer_class = Ucartserializer
    queryset = Usercart.objects.all()
    permission_classes = [IsAuthenticated]



class Ufavouriteapiview(ListCreateAPIView):
    serializer_class = UfavouriteSerializer
    queryset = UserFavourite.objects.all()


    def create(self, request):
        
        request.data['user'] = request.user.id
        data = super().create(request)
        print("fevourite qoshildi. ")
        print(request.user)

        return data
    


    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    


class PostListCreateAPIView(ListCreateAPIView):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = Postserializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetailAPIView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = Postserializer
    permission_classes = [IsAuthenticated]



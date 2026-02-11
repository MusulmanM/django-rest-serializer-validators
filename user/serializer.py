from rest_framework.serializers import ModelSerializer
from .models import UserFavourite, Usercart, Post




class Ucartserializer(ModelSerializer):

    class Meta:
        model = Usercart
        fields = '__all__'



class UfavouriteSerializer(ModelSerializer):

    class Meta:
        model = UserFavourite
        fields = '__all__'


class Postserializer(ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'
        
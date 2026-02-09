from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError
from .models import Category, Product



class Catserializer(ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


    def validate_name(self, value):
        print(value)
        if len(value) <= 3:
            raise ValidationError("kategory nomi 3 kam bolmasin!!!")
        return value
    

    def validate_is_active(self, value):
        print(value)
        if value == False:
            raise ValidationError("isn`t False!!!!!!!")
        return value


class Proserializer(ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'



    def validate_name(self, value):
        print(value)
        if len(value) <= 5:
            raise ValidationError("name 5 kam bolmasin!!!!!!!!!!")
        return value
    


    def validate_price(self, value):
        print(value)
        if value <= 2000:
            raise ValidationError("pull juda kam!!!!!!!")
        return value



    def validate_is_active(self, value):
        print(value)
        if value == False:
            raise ValidationError("isn`t False!!!!!!!")
        return value
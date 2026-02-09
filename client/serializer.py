import re
from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError
from .models import Mijoz



class MijozSerializer(ModelSerializer):

    class Meta:
        model = Mijoz
        fields = '__all__'


# NAME

    def validate_ismi(self, value):
        if len(value) < 5:
            raise ValidationError("Ism kamida 5 ta belgidan iborat bolishi kerak.")
        return value


# PHONE 

    def validate_telefon_raqam(self, value):
        if not value.startswith("+998"):
            raise ValidationError("Telefon +998 bilan boshlanishi kerak.")
        if not re.fullmatch(r"\+998\d{9}", value):
            raise ValidationError("Format: +998901234567")
        return value



# PHONE 2

    def validate_telefon_raqam2(self, value):
        if not value:
            raise ValidationError("Ikkinchi telefon majburiy.")
        if not value.startswith("+998"):
            raise ValidationError("Telefon2 +998 bilan boshlanishi kerak.")
        if not re.fullmatch(r"\+998\d{9}", value):
            raise ValidationError("Format: +998901234567")
        return value


# AGE

    def validate_yoshi(self, value):
        if value <= 18:
            raise ValidationError("Yosh 18 dan katta bolishi kerak.")
        return value



# ADDRESS

    def validate_address(self, value):
        if len(value) <= 15 or len(value) >= 30:
            raise ValidationError("Address 15 dan katta va 30 dan kichik bolishi kerak.")
        return value




# DOKON NOMI

    def validate_dokon_nomi(self, value):
        if 'a' not in value.lower():
            raise ValidationError("Dokon nomida 'a' harfi bolishi kerak.")
        return value
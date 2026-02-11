from django.contrib import admin
from .models import UserFavourite, Usercart, Post
# Register your models here.


admin.site.register(UserFavourite)
admin.site.register(Usercart)
admin.site.register(Post)
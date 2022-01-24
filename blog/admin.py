from django.contrib import admin
from .models import Post # для отображения в админке импортируемнашу модель Post


admin.site.register(Post)
from django.views.generic import ListView, DetailView
# импортируем ListView и нашу модель базы данных Post, 
# затем создаем подкласс ListView и добавляем ссылки на 
# нашу модель и шаблон
# В представлении DetailView определяем модель, которую мы 
# используем, Post и шаблон, с которым мы хотим ее связать, 
# post_detail.html. По умолчанию DetailView предоставит 
# контекстный объект, который мы можем использовать в нашем 
# шаблоне, называемый либо объектом, либо строчным именем 
# нашей модели post. Кроме того, DetailView ожидает либо 
# первичный ключ, либо slug, переданный ему в качестве идентификатора.

from . models import Post



class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    #context_object_name = 'anything_you_want'
    #если написать так, то в post_detail.html 
    # вместо post.title и post.body могли написать 
    # anything_you_want.title и anything_you_want.body 


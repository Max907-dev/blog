from django.urls import path

from . import views
# "" питон соответсв. всем значениям, url делаем 
# именованным чтобы потом с views могли обратиться к нему
urlpatterns = [
    path('', views.BlogListView.as_view(), name='home'),
    path('post/<int:pk>/', views.BlogDetailView.as_view(), name='post_detail'),
]

# Все записи в блоге будут начинаться с post/. Далее идет 
# первичный ключ для нашей записи post, которая будет представлена 
# в виде целого числа <int: pk>. Вероятно вы спросите 
# что это за первичный ключ? Django автоматически добавляет 
# автоматически увеличивающийся первичный ключ к нашим моделям 
# баз данных. Таким образом, как только мы объявили название 
# поля, author и body в нашей модели Post, Django под капотом 
# также добавил еще одно поле под названием id, который является 
# нашим первичным ключом. Мы можем получить к нему доступ как id или pk.
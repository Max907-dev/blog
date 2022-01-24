#импортируем класс models и создаем подкласс models.Model
#с именем Post. используя функционал подкласса, мы автоматически имеем 
#доступ ко всему в django.db.models.Models
#и можем добавлять дополнительные поля и методы по своему усмотрению
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey( #данный пользователь м.б. автором многих разл.постов
        'auth.User',            #ссылка на User обеспечивает аутентификацию  
        on_delete=models.CASCADE, #это указывается при указании ForeignKey
    )
    body = models.TextField() #поле автоматически расширяется

    def __str__(self): #строковое отображение модели, в самой админке посты отображаются как часть названия, а не просто post object
        return self.title

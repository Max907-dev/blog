from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse
#  импортируем get_user_model для ссылки на активного пользователя
# Client для имитации GET и POST запросов на URL 
# (для тестов такого рода нужно всегда импортировать клиента)
# 
# В нашем методе setUp мы добавляем образец поста в блоге для тестирования, 
# а затем подтверждаем, что его строковое представление и содержимое верны. 
# Затем мы используем test_post_list_view, чтобы подтвердить, 
# что наш сайт возвращает код статуса HTTP 200, содержит наш 
# текст, и использует правильный шаблон home.html.    

from . models import Post


class BlogTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'testuser',
            email = 'test@mail.com',
            password = 'secret'
        )

        self.post = Post.objects.create(
            title = 'A good title',
            body = 'Nice body content',
            author = self.user,
        )

    def test_string_representation(self):
        post = Post(title = 'A sample title')
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'A good title')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.body}', 'Nice body content')  

# используем test_post_list_view, 
# чтобы подтвердить, что наш сайт возвращает код статуса HTTP 200,
#  содержит наш текст, и использует правильный шаблон home.html.
    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice body content')
        self.assertTemplateUsed(response, 'home.html')


# Наконец test_post_detail_view проверяет, что наша страница работает 
# должным образом и что неправильная страница возвращает 404. 
# Всегда хорошо проверить, что что-то существует, и что что-то 
# неправильное не существует в ваших тестах.
    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'post_detail.html')
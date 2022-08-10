from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    url = models.SlugField(max_length=255, unique=True, default='Empty URL')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()


class Contact(models.Model):
    name = models.CharField(max_length=255, default='Empty Name')
    email = models.EmailField(max_length=255, default='Empty Email')
    message = models.TextField(default='Empty Message')

    def __str__(self):
        return self.name

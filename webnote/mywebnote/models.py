from django.db import models

# Create your models here.
class Users(models.Model):
    nickname = models.CharField(max_length=50, help_text="Введите ник:")
    password = models.TextField(blank=True, null=True, help_text="Введите пароль:")
